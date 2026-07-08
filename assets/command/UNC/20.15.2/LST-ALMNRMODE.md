---
id: UNC@20.15.2@MMLCommand@LST ALMNRMODE
type: MMLCommand
name: LST ALMNRMODE（查询网管北向告警上报模式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ALMNRMODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 告警管理
status: active
---

# LST ALMNRMODE（查询网管北向告警上报模式）

## 功能

本命令用于查询网管向北向网管系统上报告警的模式。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [网管北向告警上报模式（ALMNRMODE）](configobject/UNC/20.15.2/ALMNRMODE.md)

## 使用实例

1. 查询当前系统中设置的北向上报模式（单网元合并模式）：
  ```
  %%LST ALMNRMODE:;%%
  RETCODE = 0  操作成功

  操作结果
  --------
  告警北向上报模式  =  单网元合并模式
          源网元ID  =  0
        源网元名称  =  sourceMeName
        目标网元ID  =  75
      目标网元名称  =  targetMeName
  (结果个数 = 1)

  ---    END
  ```
2. 查询当前系统中设置的北向上报模式（多网元独立模式）：
  ```
  %%LST ALMNRMODE:;%%
  RETCODE = 0  操作成功

  操作结果
  --------
  告警北向上报模式  =  多网元独立模式
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询网管北向告警上报模式（LST-ALMNRMODE）_39656853.md`
