---
id: UNC@20.15.2@MMLCommand@LST CHGBEHA
type: MMLCommand
name: LST CHGBEHA（查询计费行为参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHGBEHA
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- 计费行为参数配置
status: active
---

# LST CHGBEHA（查询计费行为参数）

## 功能

**适用网元：SGSN**

该命令用于查询计费行为配置表中计费行为的相关配置。

## 注意事项

- 如果有输入参数，则显示与输入参数相匹配的计费行为配置信息。
- 如果没有输入参数，则显示所有的计费行为配置信息。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CB | 计费行为 | 可选必选说明：可选参数<br>参数含义：该参数用于指定计费行为的编号。<br>取值范围：<br>- “B1(B1)”<br>- “B2(B2)”<br>- “B3(B3)”<br>- “B4(B4)”<br>- “B5(B5)”<br>- “B6(B6)”<br>- “B7(B7)”<br>- “B8(B8)”<br>- “B9(B9)”<br>- “B10(B10)”<br>- “B11(B11)”<br>- “B12(B12)”<br>默认值：无<br>说明：不同记录的CB的取值不能重复。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CHGBEHA]] · 计费行为参数（CHGBEHA）

## 使用实例

查询所有的计费行为配置信息，配置格式为：

LST CHGBEHA:;

```
%%LST CHGBEHA:;%%
RETCODE = 0  操作成功。

输出结果如下
------------
                    计费行为  =  B2
                    行为属性  =  禁止漫游用户使用本地的GGSN
关闭空闲PDP定时器时长（min）  =  NULL
                    SMSC地址  =  NULL
                  IP地址类型  =  NULL
                CG的IPv4地址  =  NULL
                CG的IPv6地址  =  NULL
              支持的计费属性  =  实时计费 & 包月制 & 预付费 & 普通计费
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CHGBEHA.md`
