---
id: UNC@20.15.2@MMLCommand@LST SUBSMARTAPN
type: MMLCommand
name: LST SUBSMARTAPN（查询智能分流APN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SUBSMARTAPN
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 智能分流管理
status: active
---

# LST SUBSMARTAPN（查询智能分流APN）

## 功能

**适用网元：MME**

该命令用于查询匹配用户签约APN智能分流配置。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SUBSMARTAPN]] · 智能分流APN（SUBSMARTAPN）

## 使用实例

1. 查询智能分流APNNI，可以用如下命令：
  LST SUBSMARTAPN:;
  ```
  %%LST SUBSMARTAPN:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------
  智能分流APNNI  =  APN1
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SUBSMARTAPN.md`
