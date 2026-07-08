---
id: UNC@20.15.2@MMLCommand@DSP PCRFUSERNUM
type: MMLCommand
name: DSP PCRFUSERNUM（显示静态PCRF上用户数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PCRFUSERNUM
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCRF Diameter连接
- PCRF
status: active
---

# DSP PCRFUSERNUM（显示静态PCRF上用户数）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询PCRF上的用户数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | PCRF主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PCRF的主机名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。不支持空格，由软参BIT150控制是否区分大小写。<br>默认值：无<br>配置原则：<br>如果输入则查询特定的PCRF上用户数量，如果不输入则查询系统中所有的PCRF上用户数量。 |

## 操作的配置对象

- [静态PCRF上用户数（PCRFUSERNUM）](configobject/UNC/20.15.2/PCRFUSERNUM.md)

## 使用实例

- 查询指定PCRF上的用户数，执行如下命令：
  ```
  %%DSP PCRFUSERNUM:HOSTNAME="pcrf-host-name";%%
  RETCODE = 0  操作成功

  结果如下
  --------
  PCRF主机名        =  pcrf-host-name
  当前PCRF上用户数  =  1024
  (结果个数 = 1)

  ---    END
  ```
- 查询所有PCRF上的用户数，执行如下命令：
  ```
  %%DSP PCRFUSERNUM:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  PCRF主机名      当前PCRF上用户数

  pcrf-host-name  1024
  pcrf-name       648
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示静态PCRF上用户数（DSP-PCRFUSERNUM）_65647782.md`
