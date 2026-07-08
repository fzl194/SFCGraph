---
id: UNC@20.15.2@MMLCommand@DSP S1TAIDETECTDETAILS
type: MMLCommand
name: DSP S1TAIDETECTDETAILS（显示S1 TAI对象寻呼流控状态明细）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: S1TAIDETECTDETAILS
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- S1寻呼流控管理
- TA LIST流控
status: active
---

# DSP S1TAIDETECTDETAILS（显示S1 TAI对象寻呼流控状态明细）

## 功能

**适用网元：MME**

该命令用于查询S1 TAI对象寻呼流控状态详细信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAIGROUPNAME | TAI组名 | 可选必选说明：可选参数。<br>参数含义：该参数用于指定待查询的S1 TAI组对象名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：<br>查询的对象名称可以通过<br>**[LST PERFOBJ](../../../../../性能管理/性能对象管理/查询性能对象信息(LST PERFOBJ)_26306000.md)**<br>进行查询。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1TAIDETECTDETAILS]] · S1 TAI对象寻呼流控状态明细（S1TAIDETECTDETAILS）

## 使用实例

查询group_1 TAI组对象寻呼流控状态详细信息，执行如下命令：

```
%%DSP S1TAIDETECTDETAILS, TAIGROUPNAME="group_1";%%
RETCODE = 0  操作成功。

输出结果如下
-----------------------
                 索引  =  1
              TAI组名  =  group_1
        TAI组对象状态  =  正常
TAI组对象状态更新时间  =  2025-03-06 19:35:21+08:00 
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示S1-TAI对象寻呼流控状态明细(DSP-S1TAIDETECTDETAILS)_94695664.md`
