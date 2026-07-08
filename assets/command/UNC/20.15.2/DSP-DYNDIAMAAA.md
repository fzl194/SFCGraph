---
id: UNC@20.15.2@MMLCommand@DSP DYNDIAMAAA
type: MMLCommand
name: DSP DYNDIAMAAA（显示动态Diameter AAA服务器）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DYNDIAMAAA
command_category: 查询类
applicable_nf:
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- Diameter AAA管理
- 服务器配置
- 动态Diameter AAA
status: active
---

# DSP DYNDIAMAAA（显示动态Diameter AAA服务器）

## 功能

**适用NF：PGW-C**

此命令用于显示动态Diameter AAA主机列表项。一次最多显示2000条记录，超过2000条记录将不再显示。

- 如果指定主机名，则显示指定的动态Diameter AAA表项。
- 如果不指定主机名，则显示所有动态Diameter AAA主机表项。

## 注意事项

相同的动态Diameter AAA主机列表如果在多个Pod上都有，只会显示一条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定动态Diameter AAA的主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~127。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，由软参BIT150控制是否区分大小写。BIT150值为0时，不区分大小写；值为1时，区分大小写，但不允许配置多个仅大小写不同的host-name或realm-name。BIT150详细信息请参见产品文档中的《UNC软件参数》。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DYNDIAMAAA]] · 动态Diameter AAA服务器（DYNDIAMAAA）

## 使用实例

- 显示所有的动态Diameter AAA主机列表：
  ```
  %%DSP DYNDIAMAAA:;%%
  RETCODE = 0 Operation Success.

  动态 Diameter AAA 服务器
  ---------------------------
  主机名 域名 POD名称

  hjdiameter epc.mnc011.mcc460.3gppnetwork.org uncpod-0
  dyndiameter epc.mnc011.mcc460.3gppnetwork.org uncpod-0
  (结果个数 = 2)

  ---    END
  ```
- 显示指定主机名的动态Diameter AAA主机列表：
  ```
  %%DSP DYNDIAMAAA: HOSTNAME=" hjdiameter";%%
  RETCODE = 0 Operation Success.

  动态 Diameter AAA 服务器
  ---------------------------
  主机名 = hjdiameter
  域名 = epc.mnc011.mcc460.3gppnetwork.org
  POD名称 = uncpod-0
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DYNDIAMAAA.md`
