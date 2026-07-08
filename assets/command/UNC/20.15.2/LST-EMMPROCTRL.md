---
id: UNC@20.15.2@MMLCommand@LST EMMPROCTRL
type: MMLCommand
name: LST EMMPROCTRL（查询S1模式移动性管理流程控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: EMMPROCTRL
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- MM流程管理
- S1模式MM流程控制参数
status: active
---

# LST EMMPROCTRL（查询S1模式移动性管理流程控制参数）

## 功能

**适用网元：MME**

此命令用于查询S1模式移动性管理流程控制参数。

## 注意事项

- 此命令执行后立即生效。
- 若不输入流程类型，则将显示所有流程类型的原因值。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROT | 流程类型 | 可选必选说明：可选参数<br>参数含义：待查询的流程类型。<br>取值范围：<br>- “ATTACH(附着流程)”<br>- “INTER_TAU(USN间跟踪区域更新流程)”<br>- “UPDATE_LOCATION(更新位置流程)”<br>- “AIR(获取鉴权集流程)”<br>- “AUTHENTICATION(鉴权流程)”<br>- “CHECK_IMEI(检查IMEI流程)”<br>- “PAGING(寻呼流程)”<br>- “LOCATION_UPDATE(位置更新流程)”<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/EMMPROCTRL]] · S1模式移动性管理流程控制参数（EMMPROCTRL）

## 使用实例

查询 “流程类型” 为 “UPDATE_LOCATION（位置更新流程）” 的S1模式移动性管理流程控制参数：

LST EMMPROCTRL: PROT=UPDATE_LOCATION;

```
%%LST EMMPROCTRL: PROT=UPDATE_LOCATION;%%
RETCODE = 0  操作成功

查询结果如下
--------------
                          ULR拒绝原因值（HSS超时）  =  10
                          ULR拒绝原因值（HSS拒绝）  =  10
                 ULR拒绝原因值（Diameter链路异常）  =  10
                      ULR拒绝原因值（S6a接口流控）  =  10
  ULR拒绝原因值（未知EPS签约用户，有GPRS签约数据）  =  10
ULR拒绝原因值（未知EPS签约用户，没有GPRS签约数据）  =  10
                          ULR拒绝原因值（ODB限制）  =  10
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-EMMPROCTRL.md`
