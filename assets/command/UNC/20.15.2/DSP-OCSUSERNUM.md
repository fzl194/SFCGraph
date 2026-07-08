---
id: UNC@20.15.2@MMLCommand@DSP OCSUSERNUM
type: MMLCommand
name: DSP OCSUSERNUM（显示静态OCS上用户数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OCSUSERNUM
command_category: 查询类
applicable_nf:
- GGSN
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- OCS Diameter连接
- OCS Server
status: active
---

# DSP OCSUSERNUM（显示静态OCS上用户数）

## 功能

**适用NF：GGSN、PGW-C、SMF**

该命令用于查询OCS上的用户数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | OCS主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定OCS的主机名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。不支持空格，由软参BIT150控制是否区分大小写。<br>默认值：无<br>配置原则：<br>如果输入则查询特定的OCS上用户数量，如果不输入则查询系统中所有的OCS上用户数量。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OCSUSERNUM]] · 静态OCS上用户数（OCSUSERNUM）

## 使用实例

- 查询指定OCS上的用户数，执行如下命令：
  ```
  %%DSP OCSUSERNUM:HOSTNAME="ocs-host-name";%%
  RETCODE = 0  操作成功

  结果如下
  --------
  OCS主机名        =  ocs-host-name
  当前OCS上用户数  =  1024
  (结果个数 = 1)

  ---    END
  ```
- 查询所有OCS上的用户数，执行如下命令：
  ```
  %%DSP OCSUSERNUM:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  OCS主机名      当前OCS上用户数

  ocs-host-name  1024
  ocs-name       648
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-OCSUSERNUM.md`
