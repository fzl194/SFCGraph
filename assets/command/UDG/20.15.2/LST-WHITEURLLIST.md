---
id: UDG@20.15.2@MMLCommand@LST WHITEURLLIST
type: MMLCommand
name: LST WHITEURLLIST（查询URL白名单）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: WHITEURLLIST
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
- 七层规则管理
- URL白名单
status: active
---

# LST WHITEURLLIST（查询URL白名单）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询白名单及白名单下的URL。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WHITELISTNAME | URL白名单列表名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定URL白名单列表名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：无<br>配置原则：<br>- 如果没有配置该参数，则显示所有的白名单及白名单下的URL。<br>- 如果配置该参数，则显示指定白名单及白名单下的URL。 |

## 操作的配置对象

- [URL白名单（WHITEURLLIST）](configobject/UDG/20.15.2/WHITEURLLIST.md)

## 使用实例

- 查询所有白名单配置，可以执行如下命令：
  ```
  LST WHITEURLLIST:;
  ```
  ```

  RETCODE = 0  操作成功。

  URL白名单信息
  -------------
  URL白名单列表名字    URL           配置域名称

  test                test           NULL
  test2               test2          NULL
  (结果个数 = 2)
  ---    END
  ```
- 查询名称为test的白名单配置，可以执行如下命令：
  ```
  LST WHITEURLLIST: WHITELISTNAME="test";
  ```
  ```

  RETCODE = 0  操作成功。

  URL白名单信息
  -------------
        
  URL白名单列表名字  =  test
               URL  =  test
         配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询URL白名单（LST-WHITEURLLIST）_82837395.md`
