---
id: UNC@20.15.2@MMLCommand@LST PERFPEERNF
type: MMLCommand
name: LST PERFPEERNF（查询NF局向性能统计对象）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PERFPEERNF
command_category: 查询类
applicable_nf:
- AMF
- SMF
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- AMF性能对象管理
status: active
---

# LST PERFPEERNF（查询NF局向性能统计对象）

## 功能

**适用NF：AMF、SMF、SMSF、NCG**

该命令用于查询NF局向性能统计对象。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERFACETYPE | 接口类型 | 可选必选说明：可选参数<br>参数含义：该参数表示对端局向服务化接口类型。<br>数据来源：全网规划<br>取值范围：<br>- “N7（N7）”：N7<br>- “N8（N8）”：N8<br>- “N10（N10）”：N10<br>- “N11（N11）”：N11<br>- “N12（N12）”：N12<br>- “N15（N15）”：N15<br>- “N17（N17）”：N17<br>- “N20（N20）”：N20<br>- “N21（N21）”：N21<br>- “N40（N40）”：N40<br>- “Nocs（Nocs）”：Nocs<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | NF实例号 | 可选必选说明：可选参数<br>参数含义：该参数表示对端局向NF实例号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NF局向性能统计对象（PERFPEERNF）](configobject/UNC/20.15.2/PERFPEERNF.md)

## 使用实例

查询所有的NF局向性能统计对象：

```
%%LST PERFPEERNF:;%%
RETCODE = 0  操作成功

结果如下
--------
接口类型  =  N8
NF实例号  =  AMF_INSTANCE_001
    描述  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NF局向性能统计对象（LST-PERFPEERNF）_09652251.md`
