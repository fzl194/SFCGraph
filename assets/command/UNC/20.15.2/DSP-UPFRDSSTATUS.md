---
id: UNC@20.15.2@MMLCommand@DSP UPFRDSSTATUS
type: MMLCommand
name: DSP UPFRDSSTATUS（显示UPF中转Radius状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: UPFRDSSTATUS
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
- RADIUS管理
- RADIUS维护
- UPF中转Radius状态
status: active
---

# DSP UPFRDSSTATUS（显示UPF中转Radius状态）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查看UPF中转Radius状态。当前最多支持显示100条记录。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AAATYPE | AAA类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定AAA类型。<br>数据来源：本端规划<br>取值范围：<br>- “AUTHENTICATION（AAA鉴权）”：表示AAA鉴权。<br>- “ACCOUNTING（AAA计费）”：表示AAA计费。<br>默认值：无<br>配置原则：无 |
| UPFINSTANCE | UPF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPFRDSSTATUS]] · UPF中转Radius状态（UPFRDSSTATUS）

## 使用实例

显示UPF中转Radius状态。

```
%%DSP UPFRDSSTATUS:;%%
RETCODE = 0  操作成功

结果如下
------------------------
AAA类型        UPF实例名称      UPF中转Radius状态

AAA鉴权        upf_instance_1   异常
AAA计费        upf_instance_2   异常
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示UPF中转Radius状态（DSP-UPFRDSSTATUS）_82242445.md`
