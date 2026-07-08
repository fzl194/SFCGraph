---
id: UDG@20.15.2@MMLCommand@LST ZONE
type: MMLCommand
name: LST ZONE（查询区域）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ZONE
command_category: 查询类
applicable_nf:
- CloudEPSN
effect_mode: ''
is_dangerous: false
category_path:
- SFIP管理
- 第三方应用管理
- 区域管理
status: active
---

# LST ZONE（查询区域）

## 功能

**适用NF：CloudEPSN**

本命令实现查询区域名称的功能。

## 注意事项

- （CloudDNS无需执行此步骤）在依次执行SET DNSINFO、GEN DNSTASKID、EXC DNSCFGTASK初始化MML命令后，可以开始使用LST ZONE命令。
- 在查询“区域名称”时，当没有填写，查询当前“视图名称”下所有区域名称记录；当填写了“区域名称”，查询当前区域名称的记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VIEWNAME | 视图名称 | 可选必选说明：可选参数<br>参数含义：资源所属的域名解析视图名称。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 输入资源所属的域名解析视图名称。<br>- CloudDNS中视图默认值为"default"。<br>- CloudDNS当前支持视图最大规格为32字符。<br>- 视图最后一位不支持特殊字符。<br>- 执行命令时需要保证视图存在。 |
| ZONE | 区域 | 可选必选说明：可选参数<br>参数含义：资源记录的区域名。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 大小写不敏感，由字母（A～Z/a～z），数字（0～9），分隔符（.）构成的以字母和数字开头的字符串。<br>- 分隔符中的字符串长度不能超过63，且需要以字母开始，以字母或数字结束。<br>- CloudDNS当前支持域名最大长度为254，结尾必须以分隔符（.）结尾，且不能以xn--开头。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ZONE]] · 区域（ZONE）

## 使用实例

- 查询一条区域名称，参数“视图名称”填写为“default”，参数“区域名称”填写为“test.apn.epc.mncxxx.mccyyy.3gppnetwork.org”：
  ```
  LST ZONE: VIEWNAME="default", ZONE="test.apn.epc.mncxxx.mccyyy.3gppnetwork.org";
  ```
  ```

  %% LST ZONE: VIEWNAME="default", ZONE="test.apn.epc.mncxxx.mccyyy.3gppnetwork.org";%%
  RETCODE = 0    操作执行成功

     区域名称 = test.apn.epc.mncxxx.mccyyy.3gppnetwork.org
         部署 = TRUE
  (结果个数 = 1)
  共有1个报告
  ---    END
  ```
- 查询多条区域名称，参数“视图名称”填写为“default”：
  ```
  LST ZONE: VIEWNAME="DEFAULT";
  ```
  ```

  %% LST ZONE: VIEWNAME="DEFAULT";%%
  RETCODE = 0    操作执行成功

  区域名称                                        部署
  test.apn.epc.mncxxx.mccyyy.3gppnetwork.org      TRUE
  test1.apn.epc.mncxxx.mccyyy.3gppnetwork.org     FALSE
   (结果个数 = 2)
  共有2个报告
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-ZONE.md`
