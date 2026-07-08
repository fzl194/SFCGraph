# 查询逻辑接口的PGW主机名（LST PGWHOSTNAME）

- [命令功能](#ZH-CN_MMLREF_0264343889__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0264343889__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0264343889__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0264343889__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0264343889__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0264343889)

**适用NF：PGW-C**

此命令用于查询PGW-C逻辑接口主机名。

可以查询一条指定的PGW-C逻辑接口主机名，也可以查询所有的PGW-C逻辑接口主机名。

## [注意事项](#ZH-CN_MMLREF_0264343889)

- 查询特定的PGW-C逻辑接口主机名时，必须输入逻辑接口。
- 如果不输入参数则是查询全部的PGW-C逻辑接口主机名。

#### [操作用户权限](#ZH-CN_MMLREF_0264343889)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0264343889)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTFTYPE | 接口类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GTP-C接口类型。<br>数据来源：本端规划<br>取值范围：<br>- S5_P_OR_GN_OR_S2B（S5-P/Gn/S2b/S2a接口）<br>- S8_P_OR_GP_OR_S2B（S8-P/Gp/S2b/S2a接口）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0264343889)

- 查询逻辑接口为S5_P_OR_GN_OR_S2B的PGW-C逻辑主机名：
  ```
  %%LST PGWHOSTNAME: INTFTYPE=S5_P_OR_GN_OR_S2B;%%
  RETCODE = 0  操作成功

  逻辑接口P-GW主机名
  ------------------
     接口类型  =  S5-P/Gn/S2b/S2a接口
  PGW-C主机名  =  topon.eth-0.canonical-node-name.gw32.california.west.example.com
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中所有的PGW-C逻辑主机名：
  ```
  %%LST PGWHOSTNAME:;%%
  RETCODE = 0  操作成功

  逻辑接口P-GW主机名
  ------------------
  接口类型             PGW-C主机名

  S5-P/Gn/S2b/S2a接口  topon.eth-0.canonical-node-name.gw32.california.west.example.com
  S8-P/Gp/S2b/S2a接口  topon.eth-1.canonical-node-name.gw32.california.west.example.com
  (结果个数 = 2)

  ---    END
  ```

## [输出结果说明](#ZH-CN_MMLREF_0264343889)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 接口类型 | 该参数用于指定GTP-C接口类型。 |
| PGW-C主机名 | 该参数用于配置主机名，需整网规划。 |
