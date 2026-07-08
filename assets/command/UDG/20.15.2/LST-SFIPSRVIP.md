---
id: UDG@20.15.2@MMLCommand@LST SFIPSRVIP
type: MMLCommand
name: LST SFIPSRVIP（查询SFIP业务IP）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SFIPSRVIP
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- SFIP管理
- 网络管理
- SFIP业务IP
status: active
---

# LST SFIPSRVIP（查询SFIP业务IP）

## 功能

该命令用于查询SFIP业务IP地址信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICETYPENAME | 业务类型名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SFIP业务类型名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SFIPSRVIP]] · SFIP业务IP（SFIPSRVIP）

## 使用实例

- 显示全部SFIP业务IP信息：
  ```
  LST SFIPSRVIP:;
  ```
  ```

  RETCODE = 0  操作成功

  SFIP业务IP信息
  --------------
  业务类型名称  =  dns
        IP版本  =  IPV4
     IPv4 地址  =  192.168.1.1
     IPv6 地址  =  ::
  (结果个数 = 1)

  ---    END
  ```
- 指定业务类型名称为dns显示SFIP业务IP信息：
  ```
  LST SFIPSRVIP: SERVICETYPENAME="dns";
  ```
  ```

  RETCODE = 0  操作成功

  SFIP业务IP信息
  --------------
  业务类型名称  =  dns
        IP版本  =  IPV4
     IPv4 地址  =  192.168.1.1
     IPv6 地址  =  ::
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询SFIP业务IP（LST-SFIPSRVIP）_91417212.md`
