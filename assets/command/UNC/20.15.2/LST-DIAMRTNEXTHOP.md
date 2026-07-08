---
id: UNC@20.15.2@MMLCommand@LST DIAMRTNEXTHOP
type: MMLCommand
name: LST DIAMRTNEXTHOP（查询Diameter路由下一跳）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DIAMRTNEXTHOP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- 路由管理
- Diameter路由配置
status: active
---

# LST DIAMRTNEXTHOP（查询Diameter路由下一跳）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查看已配置的Diameter路由下一跳信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REALMNAME | Diameter域名名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter路由的realm名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT 150控制是否区分大小写。<br>默认值：无<br>配置原则：无 |
| APPLICATION | Diameter应用 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter路由的Diameter应用。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GY：Gy接口应用。<br>- GX：Gx接口应用。<br>- S6B：S6b接口应用。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [Diameter路由下一跳（DIAMRTNEXTHOP）](configobject/UNC/20.15.2/DIAMRTNEXTHOP.md)

## 使用实例

- 显示指定realm名的Diameter路由下一跳信息，realm名为“example.com”：
  ```
  LST DIAMRTNEXTHOP:REALMNAME="example.com";
  ```
  ```

  RETCODE = 0  操作成功。

  Diameter路由下一跳信息
  ----------------
  Diameter域名名称             Diameter应用    下一跳               序号

  example.com                  Gx              host1                1  
  example.com                  Gx              host2                2
    (结果个数 = 2)
  ---    END
  ```
- 显示所有Diameter路由下一跳信息：
  ```
  LST DIAMRTNEXTHOP:;
  ```
  ```

  RETCODE = 0  操作成功。

  Diameter路由下一跳信息
  ----------------
  Diameter域名名称             Diameter应用    下一跳               序号

  example.com                  Gx               host1               1
  example.com                  Gx               host2               2      
  example1.com                 Gy               host3               1     
  (结果个数 = 3)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Diameter路由下一跳（LST-DIAMRTNEXTHOP）_09897312.md`
