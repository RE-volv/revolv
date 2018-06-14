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

      hQEMA9aTfmR7xthMAQf+KXxyh9zyaCKUqZ56Zye8hTkYH4z4P8BjkkLtGslW16UN
      TnQ/k5wT/IPBmolM6p3/upwYXuCfYtcJfO6WgsyNExuEPsTJ8wvSZHhrQvocb5HF
      jU1HRfXfXpFeEVvX6RMEaYxavip6JOBm6lPL3om13/qPNImmFZyywNCFN4gI+gbh
      Z6wOiLIJv/hWi7U3EGlIR9jFt8PnpKp//oA9PNWOxvbYo7YW5xZjJGqpnuQw5R3S
      aHfE14tqxY8pCF8mgQeRakKE/G3Qoinhl0dbL9nr+qTDV6N+RMbiXKMSpqxMnXp2
      NWlTVLnWGujFcrqZd236bXq/AnozZEgAvNuYcP6KstJZAf9XQpaOKGxPzspsl2c/
      MiQbyjxhyxKIPqe50ksjviLfe/F6L06PV4A5Eu6DybQoNqbhqP5B9b/H1Zb3KyBw
      XTS/lQB/sVf44C97cpd9pHKDh5Mpa2pewaA=
      =jymL
      -----END PGP MESSAGE-----



    "SFDC_PASSWORD": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf9GdQXRsZAkK2VTXduzSyvbiB8qHsDaXgAIEnhR7qKXpUf
      dBsz0OiP4uF3SM+R2CWMm/kBBFAslwOKpNSo8abdA2hGYYvVBA9vjTIY9JAqzk/z
      PKZ7fC4LiywNUOK5fHoEMgFaikF/LtL/rFinFZeAuJ2yxyHC599P5gJsM8WT8RA0
      c6vZ/46PjI8PwXeh5vzj4MsZnWKXvc0f0mPYiLr4Mgbxc3ZReMYPkNY7gFxu7jlf
      QMM3oAblNx9BoRznbP/fsCn9Dfe4Ifm1sJWMDyzmLBvtCaTf0XZaI1KaKa2hX8fX
      Jh3FqqdsTumYM5M9nqaQ2JFfmDVAZURSAmvvDVIlAtJEASi7WRp7vL5GMkQXJSu/
      yn9NaZxq9tRhmavtTSA3Gn8kqJNLC5migZf3P4Lai24VAsnHpmhzK0tKLqOxd245
      VchzcZM=
      =CXZz
      -----END PGP MESSAGE-----


    "SFDC_TOKEN": |-
      -----BEGIN PGP MESSAGE-----
      Version: GnuPG v1

      hQEMA9aTfmR7xthMAQf+Oy+6sp/M+W+yodQzL/zENAnK8i1xpoagINFZ9OKsVhfw
      aKv1cn33MmyKJKo1HyJnOgnaeom+n7kfwG2TbxdVl0MS1udowc9qycg7w0myfwax
      5A4zI2SRe+OMytuK0iCTz8iASfsGmEM8CaMFputS3KI/u12bwtMU/z0yEJHQLZBf
      +6RmubdhwAV6xc1WvgmjmLWZPOvVLo4P8YyZAJIo7EQltGFeu0yiWBMqbR6d68nK
      1X6fqshLSyCPLP9o+S3t25qlzysMpdIK+RZ0ZjNHoFUPBE62dhdKX7pSgrMbZ5qY
      rar6oQs5XeHwFRQfQ2Xp5Cp3jNKjGIxuypInLIsp0dJTAflKhdY8LqaXE3wVsofS
      3QSHXiq0trodBcTJ1w2QyEpBnelVlFugQcwutr5SGC/A+cLY9CH9qh8QUmBB+Ulv
      c4L9IM+uEknyTls53Z6eNXi/N6Q=
      =aQbD
      -----END PGP MESSAGE------



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
    =Egu4
    -----END PGP MESSAGE-----
ssl_cert: |-
    -----BEGIN PGP MESSAGE-----
    Version: GnuPG v1

    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
    8gyJkOZi9ZdBsPng35rvZuQIwPMtAWCk5w==
    =vyJA
    -----END PGP MESSAGE-----
#{% endif %}