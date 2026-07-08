---
id: UNC@20.15.2@MMLCommand@LST POLICYMODE
type: MMLCommand
name: LST POLICYMODE（查询策略接口的选择方式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: POLICYMODE
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
- 基本功能
- 策略模式选择
status: active
---

# LST POLICYMODE（查询策略接口的选择方式）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询配置的策略接口的选择方式。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@POLICYMODE]] · 策略接口的选择方式（POLICYMODE）

## 使用实例

查询策略接口的选择方式。

```
%%LST POLICYMODE:;%%
RETCODE = 0  操作成功

结果如下
--------
指定终端和接入类型  按5GS互操作指示选择策略接口开关  非5G终端4G接入按5GS互操作指示选择策略接口开关  指定策略接口  是否基于PCF实例标识决策策略接口类型  按5GC无限制接入标识选择策略接口开关

5G终端4G接入        不使能                           不使能                                        Npcf接口      否                                    不使能
非5G终端4G接入      不使能                           不使能                                        Gx接口        否                                    不使能
2G接入              不使能                           不使能                                        Gx接口        否                                    不使能
NB-IoT接入          不使能                           不使能                                        Gx接口        否                                    不使能
非3GPP接入          不使能                           不使能                                        Gx接口        否                                    不使能
LTE-M接入           不使能                           不使能                                        Gx接口        否                                    不使能
3G接入              不使能                           不使能                                        Gx接口        否                                    不使能
(结果个数 = 7)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-POLICYMODE.md`
