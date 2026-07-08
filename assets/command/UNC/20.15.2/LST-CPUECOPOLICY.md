---
id: UNC@20.15.2@MMLCommand@LST CPUECOPOLICY
type: MMLCommand
name: LST CPUECOPOLICY（查询全局的CPU调频和休眠策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CPUECOPOLICY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- CPU节能策略
status: active
---

# LST CPUECOPOLICY（查询全局的CPU调频和休眠策略）

## 功能

使用CPU节能功能时，通过此命令可以查询全局的调频和休眠策略。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 注意事项

- 网元ID必须在系统中存在。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>获取。<br>取值范围：0～65535<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [全局的CPU调频和休眠策略（CPUECOPOLICY）](configobject/UNC/20.15.2/CPUECOPOLICY.md)

## 使用实例

查询 “网元ID” 为 “222” 的网元的CPU节能策略。

```
%%LST CPUECOPOLICY: MEID=222;%%
RETCODE = 0  操作成功

操作结果如下
------------
CPU休眠策略  =  浅休眠
CPU调频策略  =  开启
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局的CPU调频和休眠策略（LST-CPUECOPOLICY）_53585048.md`
