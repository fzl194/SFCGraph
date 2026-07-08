---
id: UNC@20.15.2@MMLCommand@LST FIXEDFC
type: MMLCommand
name: LST FIXEDFC（查询固定速率流控信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: FIXEDFC
command_category: 查询类
applicable_nf:
- SGSN
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
- 固定速率流控管理
status: active
---

# LST FIXEDFC（查询固定速率流控信息）

## 功能

**适用网元：SGSN、MME**

该命令用于查询S6a/S6d接口固定速率流控信息。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/FIXEDFC]] · 固定速率流控信息（FIXEDFC）

## 使用实例

场景参见 [**SET FIXEDFC**](设置固定速率流控信息(SET FIXEDFC)_26146142.md) 的命令使用实例。

- 查询S6a/S6d接口固定速率流控信息：LST FIXEDFC:;
  ```
  %%LST FIXEDFC:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
             固定速率流控开关  =  开启
        固定流控速率（个/秒）  =  400
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-FIXEDFC.md`
