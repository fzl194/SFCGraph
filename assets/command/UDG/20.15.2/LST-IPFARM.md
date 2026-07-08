---
id: UDG@20.15.2@MMLCommand@LST IPFARM
type: MMLCommand
name: LST IPFARM（查询IPFarm）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPFARM
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- IP Farm 管理
- IP Farm参数
status: active
---

# LST IPFARM（查询IPFarm）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示对应IP farm的信息，包括IP farm的名称，Virtual IP，VPN属性和绑定的心跳检测接口名称，server类型。如果参数IPFARMNAME不设置，则显示所有IP farm的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPFARMNAME | IP-Farm名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置IP farm名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [IPFarm（IPFARM）](configobject/UDG/20.15.2/IPFARM.md)

## 使用实例

- 假设需要查询一个名称为test的IP farm的信息，则使用如下命令：
  ```
  LST IPFARM: IPFARMNAME="test";
  ```
  ```

  RETCODE = 0  操作成功。

  IPFarm信息
  ----------
                  IP-Farm名称  =  test
                   服务器类型  =  重定向
                      VPN实例  =  NULL
                 健康检查标记  =  不使能
                   IP协议版本  =  IPV4
                   虚拟IP地址  =  10.0.0.1
                 虚拟IPv6地址  =  ::
             心跳检测接口名称  =  NULL
      Web Proxy服务器选择模式  =  继承
  Web Proxy服务器地址冲突动作  =  阻塞
  (结果个数 = 1)
  ---    END
  ```
- 假设需要查询查询所有IP farm的信息，则使用如下命令：
  ```
  LST IPFARM:;
  ```
  ```

  RETCODE = 0  操作成功。

  IPFarm信息
  ----------
  IP-Farm名称    服务器类型    VPN实例    健康检查标记    IP协议版本    虚拟IP地址    虚拟IPv6地址    心跳检测接口名称    Web Proxy服务器选择模式    Web Proxy服务器地址冲突动作
  test           重定向        NULL       不使能          IPV4          10.0.0.1      ::              NULL                继承                       阻塞
  test2          IPMS          NULL       不使能          IPV4          10.0.0.2      ::              NULL                继承                       阻塞
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IPFarm（LST-IPFARM）_82837053.md`
