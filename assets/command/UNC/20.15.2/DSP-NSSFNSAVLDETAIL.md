---
id: UNC@20.15.2@MMLCommand@DSP NSSFNSAVLDETAIL
type: MMLCommand
name: DSP NSSFNSAVLDETAIL（显示特定AMF下所有动态上报的切片可用性信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NSSFNSAVLDETAIL
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF维测管理
status: active
---

# DSP NSSFNSAVLDETAIL（显示特定AMF下所有动态上报的切片可用性信息）

## 功能

**适用NF：NSSF**

显示某个AMF下所有动态上报的切片可用性信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AMFID | AMF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数表示AMF实例标识，通过该参数配置去查询指定的AMF上报的可用性信息详情。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~40。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSSFNSAVLDETAIL]] · 特定AMF下所有动态上报的切片可用性信息（NSSFNSAVLDETAIL）

## 使用实例

运营商想要查询切片可用性详细信息时，执行此命令。

```
DSP NSSFNSAVLDETAIL: AMFID="0004c7d76079f5a24517a4e03d90e484975c";
%%DSP NSSFNSAVLDETAIL: AMFID="0004c7d76079f5a24517a4e03d90e484975c";%%
RETCODE = 0  操作成功

结果如下
--------
AMF实例标识                           AMF集合的标识  移动国家码  移动网号  跟踪区域码  切片服务类型  切片细分标识  切片可用性信息是否上报

0004c7d76079f5a24517a4e03d90e484975c  460-03-01-001  460         03        290102      1             010101        TRUE
0004c7d76079f5a24517a4e03d90e484975c  460-03-01-001  125         236       290102      1             010101        TRUE
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示特定AMF下所有动态上报的切片可用性信息（DSP-NSSFNSAVLDETAIL）_56834605.md`
