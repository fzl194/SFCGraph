---
id: UNC@20.15.2@MMLCommand@LST TUNNELPOLICY
type: MMLCommand
name: LST TUNNELPOLICY（查询隧道策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TUNNELPOLICY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VPN管理
- VPN隧道管理
- 隧道策略
status: active
---

# LST TUNNELPOLICY（查询隧道策略）

## 功能

该命令用于查询隧道策略配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNLPOLICYNAME | 隧道策略名字 | 可选必选说明：可选参数<br>参数含义：该参数用于表示隧道策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～39。<br>默认值：无 |

## 操作的配置对象

- [隧道策略（TUNNELPOLICY）](configobject/UNC/20.15.2/TUNNELPOLICY.md)

## 使用实例

查询隧道策略配置：

```
LST TUNNELPOLICY:;
```

```

RETCODE = 0  操作成功.
结果如下
------------------------
   隧道策略名字  =  tp
   隧道策略描述  =  The first policy
   隧道策略类型  =  隧道选择序列
     负载均衡数  =  30
第一优选隧道类型 =  Gre
第二优选隧道类型 =  Lsp
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询隧道策略（LST-TUNNELPOLICY）_00440405.md`
