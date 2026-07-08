---
id: UDG@20.15.2@MMLCommand@RMV ZONE
type: MMLCommand
name: RMV ZONE（删除区域）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ZONE
command_category: 配置类
applicable_nf:
- CloudEPSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- SFIP管理
- 第三方应用管理
- 区域管理
status: active
---

# RMV ZONE（删除区域）

## 功能

**适用NF：CloudEPSN**

本命令实现删除区域名称的功能。

## 注意事项

- 该命令执行后立即生效。
- （CloudDNS不支持此步骤）在依次执行SET DNSINFO、GEN DNSTASKID、EXC DNSCFGTASK初始化MML命令后，可以开始使用RMV ZONE命令。
- （CloudDNS不涉及此限制）在删除“区域名称”时，不能一次删除多层区域名称，只能删除一层，即当前区域名称为“test1.test.cmnet.mnc000.mcc460.gprs”，只能删除“test1”，不能删除“test1.test”或“test”。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TASKID | 任务ID | 可选必选说明：可选参数<br>参数含义：任务ID。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：由GEN DNSTASKID生成，用于确定任务ID。 |
| VIEWNAME | 视图名称 | 可选必选说明：可选参数<br>参数含义：资源所属的域名解析视图名称。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 输入资源所属的域名解析视图名称。<br>- CloudDNS中视图默认值为"default"。<br>- CloudDNS当前支持视图最大规格为32字符。<br>- 视图最后一位不支持特殊字符。<br>- 执行命令时需要保证视图存在。 |
| ZONE | 区域名 | 可选必选说明：必选参数<br>参数含义：资源记录的区域名。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 大小写不敏感，由字母（A～Z/a～z），数字（0～9），分隔符（.）构成的以字母和数字开头的字符串。<br>- 分隔符中的字符串长度不能超过63，且需要以字母开始，以字母或数字结束。<br>- CloudDNS支持的区域名称最大长度为248，且不支持xn--开头。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ZONE]] · 区域（ZONE）

## 使用实例

- 当设备为CloudDNS时，删除一条区域名称，“视图名称”填写为“default”，“区域名称”填写为“test.cmnet.mnc000.mcc460.gprs”：
  ```
  RMV ZONE: VIEWNAME="default", ZONE="test.cmnet.mnc000.mcc460.gprs";
  ```
- 其他设备时，删除一条区域名称，“任务id”填写为“1”，“视图名称”填写为“default”，“区域名称”填写为“test.cmnet.mnc000.mcc460.gprs”：
  ```
  RMV ZONE: TASKID=1, VIEWNAME="default", ZONE="test.cmnet.mnc000.mcc460.gprs";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-ZONE.md`
