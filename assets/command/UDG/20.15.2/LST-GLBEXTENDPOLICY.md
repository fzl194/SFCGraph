---
id: UDG@20.15.2@MMLCommand@LST GLBEXTENDPOLICY
type: MMLCommand
name: LST GLBEXTENDPOLICY（查询全局扩展策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GLBEXTENDPOLICY
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 业务控制公共配置
- 全局扩展策略配置
status: active
---

# LST GLBEXTENDPOLICY（查询全局扩展策略）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示对应扩展策略类型的全局扩展策略。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EXTENDPLYTYPE | 扩展策略类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置扩展策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TETHERING：表示在没有超规格的情况下对Tethering前后台进行控制。<br>- EXCEED_TETHERING：表示在超规格情况下对Tethering前后台进行控制。<br>默认值：无<br>配置原则：根据部署的业务策略选择相应的策略类型。 |

## 操作的配置对象

- [全局扩展策略（GLBEXTENDPOLICY）](configobject/UDG/20.15.2/GLBEXTENDPOLICY.md)

## 使用实例

假如运营商希望查看扩展策略类型为TETHERING的全局扩展策略：

```
LST GLBEXTENDPOLICY:;
```

```

RETCODE = 0 操作成功。

全局扩展策略配置
--------------------
扩展策略类型      业务属性名称       Tethering策略类型            策略名称

TETHERING           NULL                 TETHERING_HOTSPOT             cp01         
TETHERING           sp01                 TETHERING_TERMINAL            cp01         
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询全局扩展策略（LST-GLBEXTENDPOLICY）_09678530.md`
