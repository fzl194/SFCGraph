---
id: UNC@20.15.2@MMLCommand@DSP NRFREFRESHNF
type: MMLCommand
name: DSP NRFREFRESHNF（显示网元信息刷新记录）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NRFREFRESHNF
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息刷新
status: active
---

# DSP NRFREFRESHNF（显示网元信息刷新记录）

## 功能

**适用NF：NRF**

此命令用于查询执行了操作执行网元信息刷新（OPR NRFREFRESHNF）后网元信息刷新的结果。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数表示待指示刷新的NF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。字符串类型，输入长度范围是1~36。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFREFRESHNF]] · 操作执行网元信息刷新（NRFREFRESHNF）

## 使用实例

显示NF实例名称为123e4567-e89b-12d3-a456-426655440000的网元信息刷新记录。

```
DSP NRFREFRESHNF: NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";
%%DSP NRFREFRESHNF: NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";%%
RETCODE = 0  操作成功

结果如下
--------
    NF实例标识  =  123e4567-e89b-12d3-a456-426655440000
      执行时间  =  2021-03-09T16:15:04+08:00
  操作响应结果  =  SUCCESS
  全量更新时间  =  2021-03-09T16:15:34+08:00
全量更新响应码  =  200
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NRFREFRESHNF.md`
