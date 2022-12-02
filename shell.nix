let
  nixpkgs = builtins.fetchTarball {
    name   = "nixos-22.05-20221014";
    url    = "https://github.com/NixOS/nixpkgs/archive/e06bd4b64bbf.tar.gz";
    sha256 = "17fyr4ry58fwj6jybdwy3vb7bz41dnkrbflbb93f0aaqzrpasfsm";
  };

  pkgs = import nixpkgs { };

  python = pkgs.python310;

  poetry = pkgs.poetry.override {
    python = python;
  };

in pkgs.mkShell {
  buildInputs = [
    python
    poetry
    pkgs.pre-commit
  ];
}
