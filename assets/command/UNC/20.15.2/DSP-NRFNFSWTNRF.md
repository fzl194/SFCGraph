---
id: UNC@20.15.2@MMLCommand@DSP NRFNFSWTNRF
type: MMLCommand
name: DSP NRFNFSWTNRF（显示网元切换NRF记录）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NRFNFSWTNRF
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

# DSP NRFNFSWTNRF（显示网元切换NRF记录）

## 功能

**适用NF：NRF**

此命令用于查询执行操作指示网元切换NRF（OPR NRFNFSWTNRF）后网元切换NRF的结果。

## 注意事项

每个NF只保存最新的切换任务记录，信息老化时间为固定三天，进程复位后，切换任务信息会被清空。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数表示待指示切换的NF实例标识。不输入代表显示所有NF切换NRF的结果。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFNFSWTNRF]] · 操作指示NF切换NRF（NRFNFSWTNRF）

## 使用实例

当运营商想要显示NF示例标识为123e4567-e89b-12d3-a456-426655440000网元切换NRF记录时，执行如下命令：

```
%%DSP NRFNFSWTNRF: NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";%%
RETCODE = 0  操作成功

操作结果如下
------------
         NF实例标识  =  123e4567-e89b-12d3-a456-426655440000
           执行时间  =  2021-12-18T18:14:21+08:00;
           任务状态  =  已结束
           响应类型  =  直接回复504
           响应次数  =  3
       心跳更新时间  =  2021-12-18T18:14:21+08:00;
       全量更新时间  =  NULL
当前是否从本NRF接入  =  是
           描述信息  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示网元切换NRF记录（DSP-NRFNFSWTNRF）_34571879.md`
