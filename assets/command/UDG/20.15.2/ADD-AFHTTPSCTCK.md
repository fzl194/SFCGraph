---
id: UDG@20.15.2@MMLCommand@ADD AFHTTPSCTCK
type: MMLCommand
name: ADD AFHTTPSCTCK（增加HTTPS证书检查功能配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: AFHTTPSCTCK
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 256
category_path:
- 用户面服务管理
- 业务防欺诈
- HTTPS证书检查功能配置
status: active
---

# ADD AFHTTPSCTCK（增加HTTPS证书检查功能配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用来使能对HTTPS证书检查功能。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为256。
- HTTPS证书检查功能判断有欺诈行为时，使用AFPolicy策略代替当前业务策略。
- 该命令可以指定最多256个协议的SA指纹识别功能，以及一个所有协议的场景。
- 开启功能后，对SA性能会有部分影响，详情请联系华为工程师。
- 该命令执行后配置立即生效，HTTPS证书检查功能在最后一次执行该命令的60s后生效且对新流生效。
- 本命令属于高危命令，操作不当会导致性能下降明显。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFGPROTMODE | 协议配置方式 | 可选必选说明：必选参数<br>参数含义：该参数用于设置HTTPS证书检查功能协议的配置方式。<br>数据来源：本端规划<br>取值范围：<br>- ALL：所有协议。<br>- SPECIFIC：指定协议。<br>默认值：无<br>配置原则：无 |
| PROTOCOLNAME | 协议名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CFGPROTMODE”配置为“SPECIFIC”时为必选参数。<br>参数含义：该参数用于设置协议名称。<br>数据来源：本端规划<br>取值范围：不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CFGPROTMODE”配置为“SPECIFIC”时为可选参数。<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [HTTPS证书检查功能配置（AFHTTPSCTCK）](configobject/UDG/20.15.2/AFHTTPSCTCK.md)

## 使用实例

- 开启对所有协议的HTTPS证书检查功能，配置如下：
  ```
  ADD AFHTTPSCTCK: CFGPROTMODE=ALL;
  ```
- 开启对Facebook协议的HTTPS证书检查功能，配置如下：
  ```
  ADD AFHTTPSCTCK: CFGPROTMODE=SPECIFIC, PROTOCOLNAME="facebook";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加HTTPS证书检查功能配置（ADD-AFHTTPSCTCK）_00708650.md`
