{
  description = "A Nix-flake-based Python development environment";

  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    nixpkgs.url = "github:NixOS/nixpkgs";
  };

  outputs = { self, flake-utils, nixpkgs }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        overlays = [ (self: super: { python = super.python311; }) ];

        pkgs = import nixpkgs { inherit overlays system; };
      in {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs;
            [ python ] ++ (with pkgs.python311Packages; [ pip ]);

          shellHook = ''
            ${pkgs.python}/bin/python --version

            if [ ! -d .venv ]; then
              ${pkgs.python}/bin/python -m venv .venv
              .venv/bin/pip install -r requirements.txt
            fi

            source .venv/bin/activate
          '';
        };
      });
}
