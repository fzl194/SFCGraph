# 设置CRL检查（SET PKICRLCHECK）

- [命令功能](#ZH-CN_MMLREF_0000001241702627__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001241702627__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001241702627__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001241702627__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001241702627)

该命令用于设置是否进行CRL检查。

## [注意事项](#ZH-CN_MMLREF_0000001241702627)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ISCRLENABLE |
| --- |
| FALSE |

#### [操作用户权限](#ZH-CN_MMLREF_0000001241702627)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001241702627)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ISCRLENABLE | CRL检查 | 可选必选说明：可选参数<br>参数含义：该参数用于表示是否进行CRL检查。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：FALSE。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PKICRLCHECK查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001241702627)

- 设置不进行CRL检查：
  ```
  SET PKICRLCHECK: ISCRLENABLE=FALSE;
  ```
- 设置进行CRL检查：
  ```
  SET PKICRLCHECK: ISCRLENABLE=TRUE;
  ```
