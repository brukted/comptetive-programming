with Ada.Text_IO;       use Ada.Text_IO;
with Ada.Float_Text_IO; use Ada.Float_Text_IO;

procedure a is
    str                      : String (1 .. 100);
    l                        : Natural;
    x, unknowns, bad_days, p : Float;

begin
    get_line (str, l);
    get (p);
    x := 0.0;

    for i in 1 .. l loop
        if str (i) = '1' then
            bad_days := bad_days + 1.0;
        elsif str (i) = '?' then
            unknowns := unknowns + 1.0;
        end if;
    end loop;

    x := ((p * unknowns) + bad_days) / Float(l);

    put (x, 0, 5, 0);
end a;
