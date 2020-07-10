#!yaml|gpg

environment: production

domain: re-volv.org

repo:
  url: git@github.com:RE-volv/revolv.git
  branch: master

# Addtional public environment variables to set for the project
env:
    NEW_RELIC_APP_NAME: re-volv production
    NEW_RELIC_MONITOR_MODE: "true"

# Uncomment and update username/password to enable HTTP basic auth
# Password must be GPG encrypted.
#http_auth:
#    "re-volv": |-
#      -----BEGIN PGP MESSAGE-----
#      Version: GnuPG v1
#
#      hQEMA9aTfmR7xthMAQf/UFIc+RjmHlOO6H7bT0MFD+BktB8m7l0QYBNjvSrENYwO
#      VLDEp5bLY60QaxDwEP27g2O8SiL670FRLHPvAHN4j44ddQkMT3DUUDYeWWJ1nFiA
#      Z6m+B5sh4MGOVneEjNOnFFP9rBZYVkjlTbE2YH2i83GR4iTUBa1X6htznxBUv9dT
#      hkDe0u7ZMa1qaPOvdxAUxqGTIYMmOESzRL7fHywh4zriyr0Ybplg/o7AzxXUK99K
#      e72yPzxnfz+w2xpk3KesSbLwoTF5woTS2kjtgQVWbQErOK9ggUCV60RLyXNl7O64
#      ThEjFTPxMvWFjhZHDoOxZXyU2ZEZKJ2QrfW9FWMqZ9JHAayP2hE6/1VtzsjoUK3K
#      DYigbUk9JSgki44oP291MuH5dE4gOoaWNMMR006HYEpYCd7I/pO+jjFp11P088Q5
#      Foo3Py/qT4Y=
#      =aHwb
#      -----END PGP MESSAGE-----

# Private environment variables.
# Must be GPG encrypted.
secrets:
    "DB_PASSWORD": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf9G13NuXlim8Bx3LsS6ydmFV6ioatixkXx0XOedwG7poV8
      Du0+/WGDO0umyD2C7X5pfZmmHWXVLw9gg3qJiJtsExUJkkvBsdUL6vjE87W8IDMb
      ibGvz95IBFDba6jRanymVfNNu27117v0fhKF8YEFHpl55zfg6uIIzM7CXrycfvFJ
      m3LNT8iaR8mCm4soBSHiqAYx0tSOhmbKqF7kjFmk4kugFd1rJHRHjEOt86EkM6vz
      1c4nBOAniG/WU96yOm41EiSQt/rwrzQ2daZSZH6iUYn/WgjIn52wjttuHFC+cY6h
      2OKydgQqodz3TzrAM2bztclSBvh/f9BMe392OjHVt9J7ARF1jva1Oqviq/nRRbf8
      GCwMnKPRNkdWUj40T2GnyQ0qenNkL9KQifR4A1GThCtwTWCfbXxFSn5JdSI8hpi8
      2QnoeQDeGu3JQbD1t6ukTUDwmdk0ZZfd26J+xMeSiiWKGZ6wkEz67Tb41iTSOFHr
      QJOdl4kYRMC1HIl7
      =duZ5
      -----END PGP MESSAGE-----

    "MANDRILL_API_KEY": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQgAqxPyFtQHrpzElc/d0ENkAAJGkXS0ZPIVL0raUhNi8I8p
      y1Q+IMczlWqTfT1JocUhjdWZf5nA+ueu+pvnIkc6mIbdnNiYRMeKaP1B3hPkH7yI
      /3l8b5i7qfTEy5BLOYnG2N4iZgm8hrXVzSpAJ/a1vdGLGNJDzGWczdvChGw5p270
      uf0c4OxSDKqvzMci/WPrrkgjCOmUH65FGlpNvn8vZeamk+cDNF6xj8EJbQEUchwL
      thhjcNJ+WYAseFezREjVdLk8tdw086WGgi39UzJmhVxMx/fJsCWzQ+E1YEq9yhRm
      hyjaa6+uz6avzIxGLhY+MMzPjO0i+yYDZ9ghvOx8vdJRAQmJzsgEN9GGLK3mmy6+
      xKF3l93jE8c97SOjHHI6pmFl7MI41su9NT7ZanpHKrhy/qzlvHwt2qeTcN3L3jXZ
      gyLyrArbRpXWtMkbr4mQOjbE
      =YK6m
      -----END PGP MESSAGE-----

    "MAILCHIMP_API_KEY": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf/Z7iQr+9tWgczNAGqzzhyZgBcWUZzu2VFg08WcWD5joaB
      1pV6f+tltBOkqeXP9oKXUw6UlGXyzOplwGUx/P3fl1EGQGKGQwJ4+XsxLoBNx78h
      Hqb/QOXe5n2s7eTO+cNEIiaISspM83DKUmQU478K8TMenUTq3DNBsGPVTUuWA9zk
      Erwoba1OnI4dzwri021SHU1K5zCx6BECSa/aAUd168yOg/ehj4UtuGav2XNq2g1a
      c7n5F0rS3EY2lbDnUFUZ7dMcahpUIQFn1bjmQZ4kTqf+gZRH24VSRlIPpqI5cUGm
      wd/ayY1s1mFE+siWPPzvt7PNCeWE6prydJPzYyKWWtJfAdFsjfS9pxBU84qI390n
      3cS9KaVEBQEQfMF1IDMzbbBQ8RbZK5cnh+zqDBHAI+haC3+nh7kVAa4UW3uaYc5r
      qajpJTGkjpkrAo2y86OWRLIaaH2/9I48Fov2TPVJ01k=
      =5M9f
      -----END PGP MESSAGE-----


    "SECRET_KEY": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf/ZfjG6x8fdbPdB84x4XkkYRYVVBLG9x/qVwWtKXiQ0Lrr
      kvmm1kkadYdINngwYWvQmMB3IAUTCgyTT7rvvg9Bv/8h20eFWKhvRIh6HZ4yDVu2
      1oHj17el4gVYmKYXI2h0uvvHC7/F0fW6b6eoAGs5+i9a2dHnksGpZA4JlC0f8Oov
      lwOADclknR2L5IOxeax5frHGT1IN2bB/bEK72M4JMTTTVhy+MAmffUoZEgwCJe1l
      fw/qvVBt44TGcUSkj7N0YMqj//7bPnfGQa95ngYwlfhZYioWHFtXuL2MLYtMyr8h
      1eUJ6mnxMTzEn8H8Hy3gFmfE7HnoJ96rMlSrrkRi/tJ7AQq3tb1WA3LNjIk3k9rE
      g3jKUSV+OTMqzrGVa4Qj159QmUW2MDgW6yV+lH6Omd7qp7FG/YyIi3BZfh5+jrgp
      4Sf4BivOJncHafqtxFmpLfufUfqdf/9S0jOvSMgIgjBS8cRRdB5ua3OB4nAM8D5+
      wr+jJZlwxQQW4uQ8
      =rCe3
      -----END PGP MESSAGE-----

    "BROKER_PASSWORD": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf/f4NUZVT3RWOGh4p+3xFJ02xX9FpmZkf3kAveIg1bltiZ
      TeLAW9FJjVvh1I5TLZrrII/rYczckF/EOThhCHwLrp5sMbPy8gnYyiSUrL/Bv5Zq
      AwxPmCBPb04gjEbZNUwKKyWHmx8uKnreb6/rsfHDhxflr7xUk2M2VtEmza/RDjf2
      hJiwMx1TKXd+4C72kPQ+dvyFvPlCFkReE/CLFBZmKalS/yIL1tPPbVzJ2E+0i7Vv
      bYelD+Vve1h28DvOmPAp6XnVHpSViiE++zyJq77x2gXvsja6/3bZn9K194WYZk2I
      TNFUznk3vPSVRdzzGfGcjgMNEDaN2ZvbTUPaozNjidJ7ARrijwcUVKHHEJVypueJ
      QP7JXxYcfnn1TItDNk4MVi263UOZvuDXZY8UiE5C3QSuo/0Db/xsvzzgrv71p+Z0
      8UmlrSgGq2wAXSGoomffEQExn6Dj2bTKIAVKWvtKbStLJi2ZefSIghZVYdv4tpTT
      830oMCwnOkqOEcyz
      =b/1z
      -----END PGP MESSAGE-----

    "NEW_RELIC_LICENSE_KEY": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf8CdmomEDvs0aq7jesJRyxsSEwBe+PUgBa/gBfjWS9ZPiR
      yJEuyhn00VUzQMp+mGEwJVfT8jZ55PcO8texLhvQPEnEk3B/h4+hOL8gT8AnCnfT
      moYcqYFcBdnq12iu5j3miCatHDdl7mPWckKIFlHmhAVjFt56eknnQHndBxNqxhxj
      IdudML7Ugrx2iY2DUfAsmDf9tVxoCnCX00yQwY0uOAuMAXLZhs0CRHyrLVNEqnRi
      h+cQzSiQJgA5sKqwMnkkljhaeMU6DskZOg2hKfGUzZjsvqersT04adZ0OSlxzTD5
      pl3AlCYjTU16EYv+9cJ2DBx7rntPRiPF1OrwT1T2bdJjATnFNvA7xvwtuGV/d5gG
      rqJjH8Yr1j/EQpb2LEkIyNYT9uq1a23sUzh+OhjS8fjvwQxfRZxfH0t4SC3aPmgA
      s4QeQFqdD02/LG8vyzd5yHrmYnO50TTKnMuyk8VWv2GgrGsV
      =9z5X
      -----END PGP MESSAGE-----

    "LOG_DESTINATION": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf/XImTyudxieMRl1Qh0viuEtqWfbXZMYY482KHFBHLzKWB
      dFBFideQH5sibM3iqo8+L+fA4tpHEiXFyDiCKNV2u5o93kTwdNE20r2NcQ5zTA0r
      Xqono66vJUyVWbl4NSd608HH9vRSCmDxNM+R7hJ75V/fXRXINJFhIZiDaeNKvr7W
      dm2AbKX/lbsJSLf/KFqHY4KJLFqcClMOL9c6CFOAAxYGgSAYN7YPn5ThIU78vomH
      2uej6eioSpdavHJQvvb7DYph5C1J9M8MOd0dSvLwv/YE5yVwen8LAOQuicplFfWQ
      WKm7Vw9LemvOEXcHJf+XAaSIQDky2filDfaane3cpNJYAb0WQu3/cKfhZO7nZnAs
      82u+YBP9lQPPCT7fYNvyEQin+1rJDsdv9hrKg8arWnQO1FyhjKZuiT0ZU7d8GX1H
      PCzyZp7J10n8oIWeBZputJN4vOMh/Aq8Ew==
      =ZhYg
      -----END PGP MESSAGE-----

    "SOCIAL_AUTH_FACEBOOK_KEY": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQgAq2X/0Helv4agV4fmJpdaH7ap8AnzLrw5lnLAmew9gtVq
      mLOraVsIjE2XdGpGychDhSEU+FOl3DbtwvL06psQAhEmdPiBinSOvGjeBVKj8hXK
      NbRUvQsOxj8onF8LigINyklZ6Ah2WudiGPXJ+6M14//qtdbyY0g8TkkXlxd5Siz1
      2OO2VA94nKlqhYQ0fYpvEoZW3LTOhM1zLJNoMwiOfZvIcNbrvk7Bag7yUOnt9v6d
      DtfBECN7GUz03gUYjhzr47Frot9JwUFzb+Vaxze1qgqtXHa3RCKG91ReqhXSWa6l
      OANhVpUq9/jUawxzP1iOMn63YrG3Mw9z56BURFMSLNJKAT7HI3lqYriZmIq9CMRx
      K8O3/LawgVfIcdWA+wJbuILGHEy/ak+RcQvCIaq2iwIue0HeCRBlm30a0FdGYTfO
      xZAiNb5gXInRPpM=
      =x1/u
      -----END PGP MESSAGE-----


    "SOCIAL_AUTH_FACEBOOK_SECRET": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf/aNLCdrKeGf0ZFSLcmypPgZdUtDSczXh6Cuuyzb785knh
      Vx//Hk1zYr/N8b1Z8K205Tokceenay6Iveds4s6hy9oNJB0Va5TDyKVDiSZNSsZ4
      vDfEWWoIIEzf7r2RJkAaEDshMVFEBm7BFcvrIzHpJIOaGA6rQ83UdUqIwIrN2XIV
      MZdEc4qdVaFjh70JoEhfEYs6hSZeYWHm0hhc66ke4j5SYvi4/5iTOXYdLIhxfcci
      G4e9eOu5Q6Bwf/PmdJl+XdrGHvFaB2Fs+1tg+ivRK1DbcrEaVrJ88AA2boez2inJ
      2h0V2qjMYUYq4gHwdlZMsWG69ofT97YQ90XmcoX5AtJbAR88ZKXOerli+pLB6caB
      YzQIUAe5sK8U5iyrRQnof1f+VclY0Rtnx0xZjEdMMkAS/K+KhZJYFqIfKLgCrmrY
      5uKuBR4V5ZxtSWKI+ZEhQ8Y3W7ctW3s6JbJArw==
      =MOEx
      -----END PGP MESSAGE-----

    "SOCIAL_AUTH_GOOGLE_OAUTH2_KEY": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v2

      hQEMA9aTfmR7xthMAQgAgkVqADiOB5i9FqZUmxVb8sJ+WY0ZKLNjwUGoRFtfbJ9a
      YVC8AdqbsltGa4UpRCyBlWrF0yRYSGGspNi6M7h3p9oG9ARQP1AG/YOztjEig/Ya
      QEdkDw5gcDKzeu5ZxXoqLcpzaV+M1wfkz0sl5zEa4Anlk5SyvMnyK6qy7xRS/P6j
      sQVBFx7H6f5npAQ4XlFhCCkn38OHA2sm77m557fC/Vfz/jBOSRQ00QgBiNat8Ctt
      QcgDWkrXxY/3NRszkZ9KEtk8HxHwlEe9dOuhmYfD5zOHDXEfIMitSZJ3kzTBg4X3
      twpsRrq1GDZBB415K/LtBIhcbDomb1keW5t5loxH8dKEAZlv/XboXSqJQ7OMKIoF
      iiT7Bi1Yn2nnPyy2AY94ZBVze1SUNI+iKJg9YX6pImBLWPPUZI/r0GthdfWosJev
      YHlVC7MlYi+xqbYghbhBplJM9hVtvawo/4a0XWMojrjWsot2Vo8LSRfyEB+BFZZ5
      g9zEeq3kcAH0pzwQ7soAjnyowSzA
      =Wr4k
      -----END PGP MESSAGE-----

    "SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v2

      hQEMA9aTfmR7xthMAQf/ZwKuQFiVa2mNpRWby3tVhEibo7+Evh4ulwHdJXgoEM70
      fEPQQlu8e9Nx7RpGPBoElC+RmbdcqiD3V1kc2ILc7NBB5Ci3zJny+Dr7wgqID5Uh
      k364/43SuVZsPg1wW3bZh/MxqFEszg3XzvX8YN7H7uizkbn6jVuU2SfCPqNI1+mX
      hoZ7MKZ1M7hb6cjMeJhiJfA15gDnBCD/PgROamDZS54dl9JxsjEsDGNqJIADErE3
      FHGyr5N1a8KjIe/9yPZt2gAGuU47T9T1dARrSU2Dzv1OMNE44mjVfHiV1hP8SWf1
      Gual5FKANWnHF8ZQ6FoFC2R5t3+C+Q+fYD91xlStV9JTAW9THTPrnFfT09kP26do
      /peIis30+euuW8dDs1HfRHwiTntI+1ZysIb94puXzXctQyadHwyuEc6tIBABYgBI
      /9naFeVCvFxlWWjXZbvph35dtXo=
      =kIc2
      -----END PGP MESSAGE-----

    "STRIPE_SECRET_KEY": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQgAoGajf/jECL9UTaQrlP+WSYc5sgZFM/NWaKzJq6bRElWT
      ZnG5Yk7n3nmBB/yIwVu0i6xX4ferPoXFqbeeEUcsczoBPNLGNnxDQNc4UQSstcKu
      6WASMqF5c+xycWrgmOeONO9cVpbt4gZkr3sGm49NAJ5BXunewhJh3Rw6nYElvC6u
      PUfC0QM7n20+gB35sHsggjnktiUW5tx4giiwoqoLGIJJdpkAUtZ7jyEfXirF5nM9
      RihVvt3AJIZ8BrG+6LbeVFWMsuSejCkZ7hQfU6N9qVinEp7VgLIkQf57EE9/XqZo
      LF8+BOHq0NKONfpSU9ptTscpLTQlYpVz1nn6tNGBT9JbAQi8EtS+UUXknkvsHfdz
      SNrbiBAfDMs+hRS75RMurJSMSctK96Cx4abhQ/or0S4SX4ZUnlp+SWV7Jedv31Yx
      L6Nf9XBit4KFfqSBvUmPbMv442C7AfQwmaWUKw==
      =LXhi
      -----END PGP MESSAGE-----

    "STRIPE_PUBLISHABLE": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf+Lqe7JC6a7heBdNgOCpXWzL1Xqcj+G/zqRtXMp59Vflvm
      qrbq2i4kFA9nb7gZbO1WSFEwHpTqc5UuDUMfFsFxhOy/t7oq+7EZ6b4nkxPYppbV
      t6ymGWtKI43c+fKtIvkdqjygMFK8dD9Mhtx+m/B25+ZJJ5aWoFQ83KKoMeFPdjoR
      MbyvEzg6XFYljfLFmDfPo2hqyC83J8QEkyXNwEmLQTeJGlxyBInbIg32c2IvcmsI
      7/u2O+g5UuMQ4etd7Fx4K4prWQXwa2Xodc19jbct3xWqw2ME02E5x+XdmTnANGdj
      af0b0mI1206gZH0C0ymEQk4CkuLipqJSjPiaMJOajtJbAUH6nOGuo5t5luA1atpx
      Z77Pncgb0sE2rJxcAlvj+ScAKRbuCWzLMBz6IYFAZjBvhqZfCNHrD9fc4xEjccM9
      cb7Q6NPQr9D54AdWk9eusGsEMiFH/MqEOK6PGA==
      =jo6C
      -----END PGP MESSAGE-----

    "LIST_ID": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf/UC0/fl3PSPW4eDWaTFcoUpyyxVp9Ah7uCwhsBp214vfO
      hNbw1z9r1dU10D+dkI23qjSUce0083k9osyPXGEkA8xjYKZ4mOqlkZykm6JvM13l
      DEDn6WdHjRAGv4Zf0cNdXRMeYd5nD8yccX9DqW6EhmsyM1L8SaHpn87tqBe8RL7K
      +nyNCMvIi8kKR9L0/lerdp/rT8GpAisqGlcFja8cLRGwerNth+QkEy/0Y0ux60mk
      QRysBdHUIg9lZEAe73FOI4GHSiCw0n2DcUq5QX+1LqHJ5sq0zKwjB9FzsuIouWe2
      f6kJLOx8hHAaRIvOt/w9YVqgXRAL8BkLXQwNXQWLt9JFAdn88YXOaSEhXR+cJlUt
      zRDCrdXW0SZGV7mafwetT5vGG2tbfZFvgRR7MPxrhjHLl3FMPDBIPDdy1F4eVz4K
      mMZqZOSv
      =nRJY
      -----END PGP MESSAGE-----




    "SFDC_ACCOUNT": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf/c/4z6C9hZ+FqwK2jYGQYYCEv/TpMFZRhgWIKQ5ID7GxU
      mNdVDzlsK2cz3Twy0g+TKk0F7CkUHNWF3riWDuEsCESpANzQZwvIKUz2oetueVVf
      WMWGs9cAtLaoGLRZrcaKhwiUwgT6g0Sx3qK63/WlXpbnIPy/ISH8ooH+EZg4vnkR
      il5uxTbu/N4u4x0XXKzSbihViDSzpZMztoK6AudrlCiSJ0EBY3zKpR0DTiA1FVkM
      7zO+v3nD/qkih9xQeQw9/mUayjxUplK97kwvEmFeGYhFanOVIRV/aOc+VhvH5fsa
      WvgNhqy5G2JXxgfIGwx2+7gBE1LWhIy5fjF3IkDMddJTAdCIKGfHgEtz5oYL5k6m
      G0tGj+vLz9WHLrTuHm1CfVDnRo0Ob+poZjuFbNOIBMzSwExD3T4w4+MnZiSshqy6
      5hQnLZ7/g5QVPpTHfKSKIqnCAFM=
      =sK53
      -----END PGP MESSAGE-----



    "SFDC_PASSWORD": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf8CMKydgjW9WNdqlu+NXH3yAACxSniHjFEHyG3g2LpSEDm
      D7cCb/tAx5nkb42NI1zkU+7F19YrqYSOs8QMq1faXDeS192frE6Jv40B1CFdhJZ+
      JLJLyP/8API/x5OKpWLskNgCfOAtjv3PZMb1caHIPcUOj5bUFTGwz9J5m0h8I9u1
      ZO2yunL4CeWfewdnbUOG4Nc42gc5R+8xeSZKuOQRu771Jm2XJfxk/G5UiGce3Nz6
      cwxbHXmoUhqATTqKsdaG4matnMnsXmDx52i8OEAArYXsDAALtt2r09BsA3Kiclm6
      P+z+AhVhe8Gbz3fIsdjZqAjiytQs/Zo9rU9ZX0gHv9JGAf2tqrqmEA5rTh8uGK6V
      NmyZwISXMrDhwdTXUjKSdMsyb97EdvSCni8Rqivt2uAhsqfOh3OHufLEXamhurxB
      Kcev5rIYZg==
      =L/vQ
      -----END PGP MESSAGE-----


    "SFDC_TOKEN": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf/UHORpIP7hi2fIKT9CC4odzIy6Ht19R96EHOINOmqA/bt
      qvOgyKaraf8iKfyITVAbuarxEhFQJ97THChrzfIGcTTlfWcQuLfGyebz1MX9dhZF
      xzIhHziz9gYmtDWiQLz8bDa3BoRLL5H1hSnR1e6Szt9g1+nx/2BGnzrH1kZfrsjI
      PVJJnKswmtxdYscatgHCN/cltgGPAjYs9t5fc+LGuV+nfM/E2THktP2+jd6unpaq
      DfMWnBiCOqNtFnJKBbEEqfGVlvYiNXcG7e22WgBb4FIwO8Rdg68tN2ugXCAyeaLA
      euxaGAEpkI7H64bRkqDMQ/aPq0/2Y4MUGieCuam3WNJTAXuehdp8WZnrMVkzPqQ6
      Cuk7hRDtJ84ryhFue6VDDBJiao25irU1G2m8wAkENuq0LG7/ZAdcesxaIXlufSSv
      dVEX0BbjSZpbga5+bxzcSfKRUZE=
      =+qmd
      -----END PGP MESSAGE-----


    "CM_KEY": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQgAvNete1mwaF0X0O5rWp05s9bAcZqaHSpLTbHLxUh6NW2k
      6jLtPi0mYDTn4FrJBvpmacS47yO0C7bbz3kOwAkqcwoWrpxMTQAxEXuEwcloXZbl
      OLKZpgLCNrcu0m7Mspkt+BURi1SwJlSLJAa2t8z8v/CgDRWNB5dVSRkFp+1Ep/5/
      LQ748C0usXlX9YHh0BE+8UbbwhdVBNaGaeuOWlb/o8UU+XAENVuTbIY679taoBY1
      BU/83WlTH/cnTcrjK21dhp3ZB1AzY6HlLAVgQZ9IQhxXT8N6JbpPGtVBKXgLX1BP
      m4zucG2j+XTkms/oGWJ5jwcl4LJa9zH2VXPtXvHX+dLADgFwpFUoolrBrsRUcd72
      y0Pg4vaNmG7Nmt2TB5YxNRbPD8waCb7h/7cTk4K2Vzya5FGK3EZmWiRJEAGn/rFQ
      FPJWna03HaJ/xjmcoThKynhP4q1/BWnD78Y70mHH7bqFu1resiTjUA00GGhJf0Nz
      ruDNxfQMJMvwqIURSbE/4Dv0ygRpDYS21ewOL660lIkcFS9SePYblpzSbmYP9XvI
      YF/A8nC49ulgAkw+MnhikeK/qAjb4cPBKk2yCEn9b0F12bOt3UxGfxzfdqV11D4v
      =PP15
      -----END PGP MESSAGE-----


    "CM_LIST_ID": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf/SUfB/td02x15QtjS6zOlgUaqMJiAY/fyhvv/2xNHmesk
      oQhYWVruHk1Ke3cGKeX71dJruJr0BsvpdnlJXf2YR/mv8/pfYWF/WzDfbzL1Pmff
      rxXNOAP6eS/UKW68R4Ujnumo8TESQkNTEufdp6pCUhMM/tH4lzwuOFYpIwZRo8A9
      GARyAkf9hUGXstXj4rwEmGby3impo28fK4suKG1Pr2+jkqhuUx/FkkBglUkJGWrK
      z0yaVAxmQiAo4L9Ocx1z+KmNRAbcfYelw3JPtn1DC8uKlVmMQFbroFlYVWo5ZaWi
      ntrMvsl9PQXuGbgz1r12WpedezbkQRPAITKbGmCIBdJbAfLm0x4kRxRbn+ZThbW1
      ezpBoGAeb/0Dw1hHaQPHoNLUKGPhJGGFEyStPxVXQ1qgMAVKZA1+WCQdCfHo9HIe
      QYQnZV006MGKLlY6czZKQLm49nKbB4e4v/mAmA==
      =uDX1
      -----END PGP MESSAGE-----


    "CM_LIST_ID_RE": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQgAuoDo20XmZCti968vKiqvVChSamURLaw/vZO63x5BPeDp
      oc6ZPAwJPotSbyTM1fn/5F6+nGI7LU+7Zr7X1tLAHn3VKbsbc8Vi4qLuFXqyJqdu
      1NTCrsKGi1UAjyVb41CMqGJLSaTctFcbEuOqK2xSvPr6K/kxW5f7LfYYrVnUz/so
      kyUTPHGOphx8koGaQpRtxUbL9fINCe4M0iUU5DNEeZhYEv58jabUkm5ZizQOHjUU
      HTOFrERnsDbx8cBpiWYZtrhlDfdaCatCyhKOOc6WvJqUlHPp0W5nW3t30jocUbxq
      jpzW3x/XPVBoX8ix7thNSJkXG3z6giIajCJIUj+kmNJbAbc618bs5GgI7UdmOCao
      54tX3tQFNjWgEYexA10CZczci5BJLZL5AAOrV1hcWpiEYy5Qypcrp/o5H0BpJPbg
      jqPRdbYTEMmSi0NOTK9bd+mZlyucxcnNSSAwug==
      =CoPd
      -----END PGP MESSAGE-----


    "CM_LIST_ID_RU": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf/ZR92f4s92BW7qeH2CXejM+FwaxmBgp+8v67fPgH/OTag
      fd9ZNI/SPu9xb4XDWqTmFA6/KT8bxlmFna9zLgnO0+W3qbY/jy4iF8uQqbKZqGNN
      cotn+Ol5+37aQ7Uxb7fBcTnXe8jR4yCzbT2XexWRgJ+nLtQJXqDRdTjn0F+HwCFo
      eY0GjlRlCep+tnjG5MvRYj65bxiSbsoq4ZBopm1jfxs/DJU9zs4AYg6QWCJVv5ie
      aAr2GiSzBNKB1Pj2oBxBXhI2Sd+b5XKr4b/P/Jo36hX2KbNkC1Vxhj3vFktQMsKy
      x0dwM1/QVJCmE5ZG8tqwjXE20aNMJYokrFeqpjEWZNJbAfH85bZSY7VodidTNm22
      RBHn/YVDgvaM+kk1BfMyiuxoE7CT7TMQ6SwwjhpnLei7qfGucb7faU74FUPfeE3K
      5/5O0VhDMBOHkaoZIVXc1+PTzIYMBb9I8fkBsg==
      =MLMN
      -----END PGP MESSAGE-----


    "CM_LIST_ID_SS": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf+Kz3i9bZDj8emODIgz/q1us/oC8U4U/OZ3N6h+lh4cQt/
      4hxo8/aQjhljFNMzF4hLJnyEn1p0WPcypvwEucZSbQ3OwtnVTbwaDZ25azRleNU9
      /wLwDrp7kkgC38Gn/3zCtHOjMEUX69ApxBOTY0tNiYhPM5VUveao5DgIwfsP7fu3
      fBs4O88enoBiimGNUI0YDBmA+Vp1oolUqfpJ6+8Pm+/rNDOEJuLQcNAFEypCFScc
      uPDviXXTriBhPJoSF8jVo2h1aQOTCFnB1bafPi8dIED7aAbfU9lrZb8tKGbLukAL
      qqVvZb+7VPxWH52l8kNDQAQk8J7wVLtZmF7KlcRleNJbAY/dpOBbsO7Wxlov6cl5
      W5xxcZ4yDo+xW2649EA6qoFf4IKkuqGvhZMqEtE58icnA4ge5kYX02Vnns/BsUcH
      M8eCJ91xOuXjcrgqH9INcjr9kiBq+vKKHAwWrQ==
      =otgL
      -----END PGP MESSAGE-----


    "CM_LIST_ID_DC": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf/XGv19Sjphpvyod5qNtmWqXC7WmDZTEU8o2i5Gznz0a5P
      zv2QjlLQ1c1Y1eXgveoDTBsPyIy94Oglc0q5ISUgxZcyhYX3tP1HMMajUtVuvJtD
      POdpOfb8yBVzHPYq/snjCOCTDDr6SxW/8e1IZWHchzY/8Yyb5j/oCh0Lr8GJnp5T
      q7pmeAPS7gs4gwe/B4YowZS5Zl9hMZWzdNcfJdGhz/3jYIbaS565rmoz401nGKw6
      V0t4cmZ/9azkrDBYx9ihm8nsOxwFLLkNr8+iXim0GD2ey1VtL9pdfI7LCUGJHAfR
      Aj1MW73P+3G+g3/5fpcBvxNGUPWVWZqaAUUR1cnZqNJbAZBddXtth8TOxD4LT/vF
      Bc/riexI4AIW/Yzd5mDHGmx35c9pPKEav/AlHx5J8PFrnKQwLRWJECNshG3NS8HS
      FVKwjnpjjZhLwTVue2oCaDnZstEA/G4OLP4snw==
      =Np0G
      -----END PGP MESSAGE-----


    "CM_LIST_ID_NA": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf+NLaz+splt30OjuS6GS+KIPNFneHS2cSLox0lLr9tJvUU
      Rw0lhdlMKurpdy0pQ3Y07mPu0QCPZxTVYtASjItWCNHTda0v8NgwSsDVqQAzTvvk
      nGwf4J1rVOQs/MOK8djDsupLqKEeEfy0pljqXYTdGAcIXooolcIfQiIRvSamvzS3
      0hi0PEzVoSSkdXlN8exSyDiTOnzgBZuOaA1nXjhSG0wdF6XsBseoM74aWahivJdG
      nRapkPtIAhjHoWbUSjqz+VH1cy3dz9E5tn8pG+knW2DoWmKcknxixeBiU+pD2Y1K
      z2djoP8ImZ2IXLCGutN28xpCvfYwp91uUbWVrjkcs9JbAajeznE6DJfS/1kIzuHf
      +SpJg0xLYV6Ca1z3S76PNQgGCQdv/fLsymSXiMxGjx02HXXKAAui0c61yxUSAecW
      8hXQAAKFjtsabav5vUj/xrUc2PqSaCGEyxCkQg==
      =0Txd
      -----END PGP MESSAGE-----


    "IP_STACK_ACCESS_KEY": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf/XHYT8+Qx7hCZL6wRkA7JF896HxJhVEXjHWWfBKXW6n6s
      TXTS7pc1z54zMjDdt7QUTMxhh6apvz1hj3TEqV266ZKciBsDXr85iRKY3IQZjyac
      isDdkrYck1NQEYyh6eJTj254mjgxPFcoW6SprEBxO5kn6zktqhNgIz6Cr3gRu09l
      gDVzcwYawvuBAeoYMIQmzZyakwBRuDzOByzfSKPxAbRrzDdzrvPPpnaXm0wXss0B
      BRo9APcNbLogsIgcS5o+EHQK7cCs4nmTcKjy0ZLTVOzhmQXVkjF15mULAA/l/WWr
      yLANahXOdCWxxa+RChsLqIYWX3Zulf+SrPrU5BMKHdJbAfrOnpihmGLSyRvPRlND
      Mw9B2KP8EdFBDKoA0Ajo2UaScKjUqkTd68iMDgJH5xEOdYmJbsUNjydgoV9WycDc
      I6+TDr+h0lnKrAUsBeNKEcIy+T9jCmtqqo47Rw==
      =zmNn
      -----END PGP MESSAGE-----



# Private deploy key. Must be GPG encrypted.
github_deploy_key: |-
    -----BEGIN PGP MESSAGE-----
    Version: GnuPG v1

    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
    =rJBX
    -----END PGP MESSAGE-----


# Uncomment and update ssl_key and ssl_cert to enabled signed SSL/
# Must be GPG encrypted.
#{% if 'balancer' in grains['roles'] %}
ssl_key: |-
    -----BEGIN PGP MESSAGE-----
    Version: GnuPG v1

    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
    QXwPLWF8y9EMSfswYA==
    =VVoZ
    -----END PGP MESSAGE-----
ssl_cert: |-
    -----BEGIN PGP MESSAGE-----
    Version: GnuPG v1

    hQEMA9aTfmR7xthMAQf+PJN9Qu+2l+3oUj4AFxGGoapiIGV176Fybx8zT77X9g9E
    Mr/evTug+z/7ssdL7oM3rIFRkEv9lJp3Q3X+cKNoFPLRrlVGaKhOcDhK3h8NhQk2
    WEIEEWegiqDWaShyUNoXkA2TwSydwcT0SL2wdTdEOEoX8Fc6+M3KeLDCHwssmBuN
    DKII4t38zNEKixswQ4YbS2kR0S3gccHv/G+oIxezpwz5DhpLNWzubkrRepO1QlLh
    fvOZgUvjnq1NVNtDw7gYgSnojVw9EI8F370pW7QyD49VszsqsLye5vx3Fv2EbwyX
    XZzjrwieFxQH7jBe/gy7ON7+jBSOPix1BW4BkeM62tLsAUGsWFSdbEn/8sy4Cd6n
    Q9cvpajhlCtNGyCakuuTFTxrl+FNmBNRafghj0LhHGSHtqk2d1SbcdC2VE0B+maD
    V0YF+Tcsd2siaAu4Q0Qs3VONRPIc3jdke2b3nTUWfRcFgTrRlWDMjpiPQOmScCQ9
    LskuGm5ccHUdFs7eWVPhBodtxoo+3O0ca0aHpFRe9PIP3fYZS3t+tbsHHWXUvuvH
    zuhL6/K/aYtDqUhgJCc99hADqSTSKyF/4Yxv03eCetj35PgsAeu2lXx0gre1RL1r
    YHOHJyquPa4wX9yyJVmjiDxjU6+BnZ+n1+MN4ozouR+0/W8eBrs6qctOB9T8URYo
    LFYJvMx1BsI6oKrt9rT+Z3X0YtS6+Ol3wCpgBBUN1dpURL18+yBMNO5+P1mPFvGB
    AalyyP3eZbyCE27zbLEcwqQKtw7xSL5jG+N9hOG1YQ//Brib2JYewkBdzy4UzOzH
    J0xT+Is1FDoiC7QrrLjf11RuKuS6wT9cCzWzbwGdpkF06tKJeGSoUOkGbTO2dPub
    zT7mWvUqByuvYxP4c05UqHlGgJQ+R+SsHB+FqAk5Rsg0d0bPyNgWIA8SAcnKMj45
    gFM+h0JajIFSXVCHjMXSG1dSZmR3MqjS5+W7zq6sdYcgLxD2yEiqElbVzO7QsPY2
    EVSHRx54SmytfWF6s2d3cFHImElTW0Rde5aW9Mcdcl3OqIxttUrNah8eiFQ2snB3
    KEJpBqNXbTYF5z2UeAllYgfEcl9J/osfvnrmrG8IqZ4LibNwqxQ0me7H5TKU6k63
    7rWxh7fwuxvZCwocY0JMVanb2ueOSmZnTTgwtrA06lVIKhjg9yLCJOpdFVdSGhMr
    8IKIdLkwWWTR6yDbx3Q1pkDuu7vOVEACDSfNGXwFSJfmZCWTZiC9w/0ScrH/HZwB
    1q1hxwVU4K7kP6YEh4fNT4TdAQvo7VXZiN/uXVIdgujcm/Z2zxO8jNR/mOekeJMv
    raTuyDqprHLqibSYCyqXegIo5Bwli1n1vlrTbt9ItmNOQDo44FZhpFYJ2BLA1BmX
    3lCUlKFkLGTaZiRdVIq+qOt4T5RClRUQEOlQv8nuNPNhSp2Xr96d2+PaWxQhGDG1
    5+vMad0jFze0PJdnD9/CJz9k1ZjZxApobZ9KdB6VJ4YLUPHSypvxQ2uNddNK6xlp
    jRD0HD6kLFpxIK9qYvLK2N3kdAMVGfzlYxSpeXN85hNdvhdbcmKQsRehPKUp2cTA
    tAwrpQvmzm/IzzrI2TPwTCNSkYHN3YXi6/o9FDOOgeQq+OUjLK2sHY3zKuU3zxaI
    sg+EikVPXaOF6BNGbblwdEZAuk95Iqtx/dqJG09J7ekC0IhLrWbGsD2NuZL3pAXX
    5QM/9xBpaI9rXHU2YsG7n3ecjEpdXOTrsxA67WEGxLk4fa3c1xg2ImyZPT83+chY
    vaP1Ol2MVBE5QRSqAmjwkmIlW/IEue25apH+t5cp5gQp6v2K4LUvvIxXtehRaSbJ
    DO/sm0KEoZlHClx1A0GrHuOW2f0nvGLloXLVVHfGr8zykEiuG1a5hI51lgp3m3Yk
    5kCc33BaL0fofxrJpXS8iQQMSZ0uxRKGuOXVnph4NV0AKjz5dWJXIU/ZYTiEyRJg
    Yb/8n0BX59CZMZsgZ5+fP4TEcXoCXb8+TcUFrLAhK4y1lan5hJlXmo1aC7F6dUQu
    8ChGyeAvD15EtF3RJAXmbqmPCzIhiHBpMo5OPrA5cRzg6xFY0KkCBVpsZSnjpLtD
    FgZwQcnT7GUpW1tOU2WrXOIUvMjCfexBO/1R1iE2oEtPoywHrC70/7wyfGGVqzte
    tnVrEXJpX5hQg1scrESLcHZYG+nJ+ygue5fYN6WXn8aGtt5dU85086kp6mSvyTMs
    MnAEa+UeYj5QKPckUcXnhHqCPtZ4txDkYfMZYwtakgVH4W+xX8tV7fm4wed60w+l
    5hyh5hV5t/qQ/dCgbzdTqJL7/jChz8l1vncO+I2myRFTQlCXbShdb7Agk7Wwk/wA
    rEfsuks5OkyKksdzWpotxeFmrhi15ih1UHoSEvBUlqBbdQGI6EqTIunxkybbZ2BJ
    Nz1TQhSlLSZsYzNADHSXaFBMeMzmYZElPzQdVuVOEg3OdtQTiV2it8M243sgghRg
    aO3r9UfCuOhrlhqaP/XeAckK8Kd8d2XJgm2To5w8c9sVVEH0u82z3zg6KdgqsEjF
    LQW89hRm/1v25gtCw8YiOd2tubHvn5lItBVhqrEVxcU+TUL0GoYQBXxjz4ohZsP3
    T8ceHqgj13gwZNS2Q3lYVfWYMZFNFaXrj2L/XdmdO9VJYAOEWsQr8hUjGro3e9Ep
    BAy3+PwrIRYe/BI7eexfMBRKt7R6PwCSgxqoDSQ6A2LZuUk2GIx94CDdGaye6cTO
    r1gpbKhu43aPrSLPireIgaGPLGAiujruPZCG50jYIW1Npn4vVuwIlBQ5zMHiapvW
    DAV6xFmf3vrX38klZM4Om7UOzEwTTYSTfxdJmaxkYQ3hY80po9bUNmhxlB0AhJ9y
    jXTmvE4gTC8isDAHPZIZ8dC4HsINO4EiECBZDaN6p5CR25nrNiZTJhlBZYlLPRVu
    iSuYOhD/gW2777w+S2T8zKueIi/s/yJoQ7888baiGezxrupvlJH5Z0B0q/GOXduu
    EJBAOcyIb9YBEVms2Ikoz9xYjFhZWsIp24biq9cQCsfHSzqdqPnCTUxElv2sxe1C
    n3ehbQzHm/zXWIm9588XPZbO3l7XO8xjyHYWnt/xOP/seAs9w5kpN0SNuUhL0WHV
    fUfmOtH3brEfRSIO1AeXAY9nL58LXBje5ZiS5fTlRO6WJHEkGGz93gWG1grauUtW
    duIK2zqxbWQwWpBr7VNeDUkAw8eo/gTmmOnKOR8LF91EHD53A6C6UfIbS1xGkGst
    UhiPr1vTdj+MvmLVl5K4YGXz446/Yfz1g0X9u7aAm9qkTFZNBw3S8Gh58yBnM1hE
    MNDsZRwPw6+DhBZZrxlkhk3vTtEcVZYJKj5+LPzeXp2/tYGoUNrHW8jkgwr3tDjA
    pQ7pJdc+lnSpEipjw6EVdmoGo+LREauvLKE0EkbAsD4CJrpoG2adeNmZ+EZlGeWb
    ALQfg1Ed7PXulyIOZxvq1fzqCHM2+zlRHYj+eYvVICSBEYPd+NiZV1sr7S2q/PJE
    HKZJdpfpZ4y6CvyM/oRsop8qzgCGaN5rWyd6wQe4WWKIM43F6fLf9NrNNbmyMPem
    SyawBPmsNZ+U2DJoPt3T+F08mf3jmwuZNcUEgwf2vKotXaC5tR+uki1sdjxns07y
    tBfY3YuEqXZX6zaM0rsJ9rYVD49EBMTcmh8z/PUStjHsVCRQ/jpPndBALfOuc57W
    cJyz045Uc7t3RAIpCxP+XrVLxsvjUqEZ1kdn8Cnb/dmuQ6SOF9345c3yjBbsW9fu
    FQUwPicOZLcni/z7vn8LZ9Tbhm/0fIBBoBw/0ttmF8ccKK/B1N5z20V7spuaDGle
    L6y4D3vEyX7fu1kYbhsfMgamEc1QYA9qTlndr86h50jy2O9t9eyI/0nQQ9tz59IB
    XIXWqTH/zqGG2PUZ5C7Y46VqJ+WTkSOTp0dAnUD4/8kAY8o12F32f8W4nV9trxUK
    cPGEBUSbquFBRDW+ghFTQ/so1PWlv3oDFKnpO5yFFQ/ejX0lXtutY+McooDdyMc3
    NYL/TvK1XYcyqaVxJwNc7EuaS/qnPZiYgEGB6+kmhhxHvJx3htRmwnboNoNR0mZE
    FuKWrcPpQR+cl9Vy+d11K2fNw+R8SHh/Fq+wiS0oflxPkZhQKg4hGEXHIMBPSAYg
    8T1wPfI+rBH1PDBFv7oJsx89mAPfLyeAoNDebI5PbSjMgVG7OV51qvOrd71rZh6n
    JF3wVh6Mtd1u5EXyXR8XV/pvxwh+MSnhbJfecuPWVLnxlqs7q/lt399rHboBxw0j
    hFnSN55A7V5fZIO91qCeAnOgwVCPHEZenDlxrezw+BbiCDQINr+dTHqgbuk6PWsG
    IiH4QIwm+gGMsMx4+AKgv5qUoPf/2Sx6ytcq06JyDacoJFkeySiv2vy0V6afOq90
    He2cThucyozAzso0MExXqvTm3diDIW7tZCrDTzvzgAzteVxA31qars6I5Xe9kKqA
    JQeEpl+9LuR0bO11PuPRJuK5jqY98l3WriyEeENNC22JXMQi4rQHTILWUxGQmFm7
    MeXTC0LcY6QG4gWil9rs7YzUijlkoQCLiDmFvpei9vZiddr0+M+TGdB44KKxxxuL
    zu2dlhTnsxkhRfCnnlane+yEGb5zKYhsfntH/TefaTsTtqg6w+3mjSvvc3sFomvx
    fr85wzzy/M6rG6l7NI6gvEFkpTlYqVSbt+MDZYyGqxr54ylgVzhHaVnh3FiiqwDX
    Y0r11WrHPmOX2nsLgLID3M5F6sxyEuHVrPgkRmnYGH//TlryhMgwaSPsarvLxnc9
    r1UdlV8zH4yny9gntYkb0Heuvss1OUe6G+UZTuM/DSL3kszDIDa7RhULxzc7Js97
    rHL2MmrY950gK9PGdDzhMgWUrl0CVyUCmwzFcLIxW7qLrUYv5PO90nIIHhaSZKOX
    dgIYf9oOwFBR/fUObx/kfTR7HfeSo8TPRqOB9yNTx1A4i62Be7WHk6rBOiPzlvzT
    k85mG3VRL9MUiLc2pvG9kYNsVVBwggh2HLEasYGykV1jiS9N+H6g5y4UfjF3xEm8
    MmcTgtsZ6Wgo6Yvn8Z9ncC2YsTHu3vOWTV7T7Y//ziQ2geGqSiP5ERhGrGjK0GKi
    gGZ/KVK5O+fozo48OBg/bWi3mzQXW+xpF/jehx1oZQELJRNMxtgUXd8F/LM2wfcr
    geNaa2neaCJdKze27JGJGTLjT53HO56OIP+D40hVpQ2ZHpD0JEsuOvTusMayFhLl
    3p/vQKHYYgdgiPA3qjMqzIDomvy9hrHIE1hIsQELDPiUm3QSU2DzqLjorCAkypYb
    cyna5zbdlfbaLS2C30kKyWvONAGkiswFsJWFQ/KuiVD9yt05rSlUucIy48/t1vja
    QgHmbGoRZKG3fGae+G4U8ew1t6yUk6SiB1Q/gMcogvfz/9RrGtCh3EGJC6hzgXft
    VG78pvCuTtQq31GxSkhHohmmzQXDZy7+9bsV143/Fu3D3HWVASkPVqY4/2hikOhC
    OeiNNSlTZx/+RmOcXhnz8C2S9lWiYjLDSVITkE5b85JWla/+WI5XUGxaQ+XjEsiy
    Iis4LETpswa2DC6Neij9UkULvojwj+uPnVL367LwkRcC68lapBTTuNXLSUmzmNRs
    H5zRDtHb9ZU8/n6ht8cXNxEvGGeTp2wtujjP1zS6KIPF8uoelgTCMOoNSZGCOagi
    QXWFt8jh5t0H7be3VksILKHN8ICaDs/OD6DCPMjwt5rriVplhtcLVkOi5yARV4uk
    ZK/Rq9YbxcGw3D4ACWfz1qgN066xCPwmnUPUFPpbg/n0A4qydOfZDaL+sQ+0IevG
    T+oe5HGkhOrSGWfK1XQXAX8v3ETfcjiZADRUk/ci36AeBCTvsGilj5p7DpJa60OW
    KcNBJG7cknrqmeWZl0mPrwImZQyY7vifARDBEk01RBmkIFaMpBsN0fcCbgzibGtJ
    qZdFkpVV2HLuW+2iY/nSwMTVWSXQH1Ho0fl/hMnuBracNG5j75KunRkOlyiXGs71
    JgnbkOhMfpfLiYv+QO+aB2NmVppXzLBICmA+WIA56EOkxM1CeDUDzLmhsjnhj/7g
    Ukfl0iI1OjplANKyKWYJpcefdYmDtpGx5BIgiC1AkQqWn38w2MpIMeHArtG6WJ5X
    gL3yEYDRIHVdzI06d62rioeg9bKB/l5GJZhehAveq439KvUvIxnduteFbpIUc8DV
    kaKpPHbk2ZLmaJxI15kTOo9rsp+vI4PAm4DivAZkV9UKke92wiuK7kAY/LQKhh2i
    mSuYP8DhistUmcPvSbQKYUYZA7AG7BCktaLoJUxGBkCD8LhLMx6iYL78hW0/FZH+
    hfwuWDQnOOLT3vXCzXfjkPP3zI12Y+W2mmoLeLryP4DwcW/5dE024gn22ObWhwff
    eWl3JurOe+4X2mtioLb/J0+CIGfzNotqFvHECRM5kStyLHRARMq+YX6fySNiU9/Z
    7TCu3odhahGbyR78nchA7+QoHCDGE6vE3Z5jEOa6iDbWL9aoyxQR+aroXGFO91M4
    LHaopT5HWgN8f6XL4rNKEs0NKUsDMstQd27vpZd+DUDR6SmB8tDFfpLa9mHBnnHv
    7oAEwuOxppLqfo0L/jclpoBlnQyKq0eJyaIzNFCAGit9c2LW7lybmhToflPrgef4
    Ww3oCAqc0R9XSCujYd4lgh+/rtQuhZ6w3vGu7YrASSG/isG2wNN7VkQTc9iJNz5v
    rx/41VsEK35SkrlsbNLMT8edMoRXDhUC4pl1/aCGD7AebCma1KqqsFhb55Wy+88D
    RZjJE1sAB3E7vVPyQ20a85OSaPoKEzV9cI82nizC03YgB5zXAYRY6THK3gZXzgxT
    LR33CKiFgS867Ctl5/feO4fYafd7qEO3dWMVr3+5/fXoduJihxk7pxxyCKDamNjC
    AL1Ad20Q/IfKmpkSBf7NusnqFNEBASXhwmKGwQ+6srOk16Q2/SGEBDqXyIKQTHoV
    nJ5B/qNYAJN0aAh4fYz4rczfgGy5i9O+OVNLw2UiOpZNCmHhHaP0ucmiOKfb+H9b
    GTM3dC7cNiCZthZbcHdkY3tvS5pKkRFGD74LjS4GZWwQCP44HewHUdGWm0Wqjb0e
    RizHGwdW3rzrJ5G2dWyH1NnRiHP1NKALxHnPqtRviKpsCr5RwL+1tD0dlWsZaSrZ
    u4iG/PHozW3tfIKvaoPbErI2IrvdumnBRt1MqCWpULbPWzAIXk1hvO24kNPo0hZb
    tq/cvp8=
    =rqaZ
    -----END PGP MESSAGE-----
#{% endif %}