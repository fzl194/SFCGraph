# 查询VoLTE话路环回功能（LST VOLTELOOP）

- [命令功能](#ZH-CN_CONCEPT_0207016808__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0207016808__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0207016808__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0207016808__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0207016808__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0207016808__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0207016808)

**适用NF：SGW-U、PGW-U、UPF**

此命令用于查询VoLTE话路环回功能的当前配置。

#### [注意事项](#ZH-CN_CONCEPT_0207016808)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0207016808)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0207016808)

无。

#### [使用实例](#ZH-CN_CONCEPT_0207016808)

- 查询VoLTE话路环回配置信息(当仅配置了一条信息时)：
  ```
  LST VOLTELOOP:;
  ```
  ```

  RETCODE = 0  操作成功。

  VOLTE环回信息
  -------------
  标识类型  =  IMSI
      IMSI  =  456645645644565
    环回点  =  上行入方向
    MSISDN  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询VoLTE话路环回配置信息(当配置了多条信息时)：
  ```
  LST VOLTELOOP:;
  ```
  ```

  RETCODE = 0  操作成功。

  VOLTE环回信息
  -------------
  标识类型    IMSI               环回点        MSISDN

  IMSI        356897584584516    上行出方向    NULL  
  IMSI        456645645644565    上行入方向    NULL  
  (结果个数 = 2)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0207016808)

参见ADD VOLTELOOP的参数说明。
