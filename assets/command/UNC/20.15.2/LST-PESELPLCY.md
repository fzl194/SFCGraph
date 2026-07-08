---
id: UNC@20.15.2@MMLCommand@LST PESELPLCY
type: MMLCommand
name: LST PESELPLCY（查询SGSN/MME选择策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PESELPLCY
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-SGSN_S10_S16_S3接口管理
- SGSN MME选择
status: active
---

# LST PESELPLCY（查询SGSN/MME选择策略）

## 功能

**适用网元：SGSN、MME**

该命令用于查询SGSN/MME选择策略。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/PESELPLCY]] · SGSN/MME选择策略（PESELPLCY）

## 使用实例

查询SGSN/MME选择策略。

**LST PESELPLCY:;**

```
%%LST PESELPLCY:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
对等网元识别模式  =  掩码模式
        比特掩码  =  0x8000
    MME Group ID  =  0x0
MME Group ID范围  =  0x0
  使用RNC ID域名  =  YES
     使用ID TYPE  =  YES
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SGSN_MME选择策略(LST-PESELPLCY)_26305774.md`
