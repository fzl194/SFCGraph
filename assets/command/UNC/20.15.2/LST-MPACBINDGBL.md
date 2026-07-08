---
id: UNC@20.15.2@MMLCommand@LST MPACBINDGBL
type: MMLCommand
name: LST MPACBINDGBL（查询MPAC全局策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MPACBINDGBL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- MPAC
- 全局策略配置
status: active
---

# LST MPACBINDGBL（查询MPAC全局策略）

## 功能

该命令用于查询全局MPAC策略。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4协议族。<br>- IPv6：IPv6协议族。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MPACBINDGBL]] · MPAC全局策略（MPACBINDGBL）

## 使用实例

查询MPAC全局策略：

```
LST MPACBINDGBL:IPVERSION=IPv6;
```

```

        RETCODE = 0  操作成功

        结果如下
        -------------------------
              IP版本  =  IPv6
        IPv4策略名称  =  NULL
        IPv6策略名称  =  policyV61
        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询MPAC全局策略（LST-MPACBINDGBL）_00865761.md`
