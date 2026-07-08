---
id: UNC@20.15.2@MMLCommand@DSP FIXEDFC
type: MMLCommand
name: DSP FIXEDFC（显示固定速率流控信息）
nf: UNC
version: 20.15.2
verb: DSP
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

# DSP FIXEDFC（显示固定速率流控信息）

## 功能

**适用网元：SGSN、MME**

显示S6a/S6d接口固定速率流控信息。

## 注意事项

当系统的SPP进程状态发生变化时会影响当前返回值。

由于 [**SET FIXEDFC**](设置固定速率流控信息(SET FIXEDFC)_26146142.md) 中 “固定流控速率（个/秒）” 平分到各SPP进程后会有取整误差，所以实际固定流控速率和设置值可能不一样。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/FIXEDFC]] · 固定速率流控信息（FIXEDFC）

## 使用实例

场景参见 [**SET FIXEDFC**](设置固定速率流控信息(SET FIXEDFC)_26146142.md) 的命令使用实例。

- 显示S6a/S6d接口固定速率流控信息：DSP FIXEDFC:;
  ```
  %%DSP FIXEDFC:;%%
  RETCODE = 0 执行成功。
 
  输出结果如下
  -----------
           固定流控速率（个/秒） = 400
   (结果个数 = 1)
 
  --- END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-FIXEDFC.md`
