---
id: UDG@20.15.2@MMLCommand@LST IPLIST
type: MMLCommand
name: LST IPLIST（查询IP地址列表）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPLIST
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 三四层规则管理
- IP地址列表
status: active
---

# LST IPLIST（查询IP地址列表）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示配置IP地址。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPLISTNAME | IP列表名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP列表名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IPLIST]] · IP地址列表（IPLIST）

## 使用实例

- 查询指定IP地址列表：
  ```
  LST IPLIST:IPLISTNAME="test01";
  ```
  ```

  RETCODE = 0  操作成功。

  IP地址列表信息
  --------------
      IP列表名称  =  test01
  IP地址版本类型  =  IPV4
        地址信息  =  10.0.0.1
      IP地址掩码  =  1
      配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询所有IP地址列表：
  ```
  LST IPLIST:;
  ```
  ```

  RETCODE = 0  操作成功。

  IP地址列表信息
  --------------
  IP列表名称    IP地址版本类型    地址信息    IP地址掩码    配置域名称

  iplist01      IPV4              10.0.0.1    1             NULL
  test01        IPV4              10.0.0.1    1             NULL
  test02        IPV4              10.0.0.1    1             NULL
  (结果个数 = 3)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-IPLIST.md`
