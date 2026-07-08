---
id: UDG@20.15.2@MMLCommand@LST FABRICINSWITCH
type: MMLCommand
name: LST FABRICINSWITCH（查询Fabric-In功能开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FABRICINSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 配置
status: active
---

# LST FABRICINSWITCH（查询Fabric-In功能开关）

## 功能

该命令用于查询Fabric-In功能开关。Fabric-In对应是内置FullMesh卡，内置FullMesh卡负责框内流量交换。

## 注意事项

该命令本版本不再支持生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/FABRICINSWITCH]] · Fabric-In功能开关（FABRICINSWITCH）

## 使用实例

- 查询Fabric-In功能开关：
  ```
  %%LST FABRICINSWITCH:;%%
  RETCODE = 0  操作成功

  结果如下:
  ---------
  功能是否开启  =  是
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Fabric-In功能开关（LST-FABRICINSWITCH）_03378282.md`
