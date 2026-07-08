---
id: UDG@20.15.2@MMLCommand@LST NPFECSWITCH
type: MMLCommand
name: LST NPFECSWITCH（查询NP FEC配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NPFECSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- NP端口管理
- NP端口FEC功能启停
- NP板的FEC功能开关
status: active
---

# LST NPFECSWITCH（查询NP FEC配置）

## 功能

该命令用来查询NP卡端口FEC功能配置。

## 注意事项

- 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/NPFECSWITCH]] · NP FEC状态（NPFECSWITCH）

## 使用实例

- 查询所有的NP卡端口的FEC功能配置：
  ```
  LST NPFECSWITCH:;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  --------
  接口名称     FEC 状态     

  100GE66/0/8  FEC_MOD_RS   
  100GE66/0/9  NP_FEC_NONE  
  100GE66/0/6  FEC_MOD_RS   
  (结果个数 = 3)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询NP-FEC配置（LST-NPFECSWITCH）_50068406.md`
