---
id: UNC@20.15.2@MMLCommand@LST OSPFV3IFIPSECSA
type: MMLCommand
name: LST OSPFV3IFIPSECSA（查询OSPFv3 接口的安全联盟SA配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OSPFV3IFIPSECSA
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3接口安全联盟配置
status: active
---

# LST OSPFV3IFIPSECSA（查询OSPFv3 接口的安全联盟SA配置）

## 功能

该命令用于查询OSPFv3 接口的安全联盟SA配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST OSPFV3INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OSPFV3IFIPSECSA]] · 创建OSPFv3 接口的安全联盟SA（OSPFV3IFIPSECSA）

## 使用实例

查询OSPFv3 接口的安全联盟SA配置：

```
LST OSPFV3IFIPSECSA:IFNAME="Ethernet64/0/3";
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
       接口名  =  Ethernet64/0/3
 IPsec SA名称  =  sa1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-OSPFV3IFIPSECSA.md`
