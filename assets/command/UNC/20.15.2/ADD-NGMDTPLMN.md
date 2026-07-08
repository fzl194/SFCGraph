---
id: UNC@20.15.2@MMLCommand@ADD NGMDTPLMN
type: MMLCommand
name: ADD NGMDTPLMN（增加最小化路测的PLMN）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NGMDTPLMN
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 5G MDT管理
status: active
---

# ADD NGMDTPLMN（增加最小化路测的PLMN）

## 功能

**适用NF：AMF**

该命令用于增加基于管理的最小化路测（MDT）的PLMN。

## 注意事项

- 该命令执行后立即生效。

- 配置记录添加后，如果当前用户正在进行业务流程，配置限制不会实时生效，在下一个流程中生效。

- 最多可输入16条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLMNIDX | PLMN索引 | 可选必选说明：必选参数<br>参数含义：该参数表示最小化路测（MDT）的PLMN。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。PLMNIDX通过ADD NGSRVPLMN进行配置。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGMDTPLMN]] · 最小化路测的PLMN（NGMDTPLMN）

## 使用实例

增加最小化路测的PLMN，执行如下命令：

```
ADD NGMDTPLMN: PLMNIDX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NGMDTPLMN.md`
