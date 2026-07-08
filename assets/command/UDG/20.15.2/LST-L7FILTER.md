---
id: UDG@20.15.2@MMLCommand@LST L7FILTER
type: MMLCommand
name: LST L7FILTER（查询七层过滤器）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: L7FILTER
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
- 七层过滤器
status: active
---

# LST L7FILTER（查询七层过滤器）

## 功能

**适用NF：PGW-U、UPF**

此命令用于查询七层过滤器和子七层过滤器，支持批量查询所有的七层过滤器或指定七层过滤器下的所有子七层过滤器的内容。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| L7FILTERNAME | 七层过滤器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置L7Filter名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@L7FILTER]] · 七层过滤器（L7FILTER）

## 使用实例

- 查询名称为testl7filtername的七层过滤器：
  ```
  LST L7FILTER: L7FILTERNAME="testl7filtername";
  ```
  ```

  RETCODE = 0  操作成功。

  七层过滤器信息
  --------------
       七层过滤器名称  =  testl7filtername
     子七层过滤器名称  =  testl7filtername
             URL Type  =  URL
                  URL  =  www.huawei.com
                 HOST  =  NULL
           客户端类型  =  NULL
             方法类型  =  CONNECT&GET&POST
  Referer关联计费开关  =  使能
         彩信模糊匹配  =  不使能
           配置域名称  =  NULL
          扩展头域名称 = NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询所有的七层过滤器：
  ```
  LST L7FILTER:;
  ```
  ```

  RETCODE = 0  操作成功。

  七层过滤器信息
  --------------
  七层过滤器名称       子七层过滤器名称     URL Type  URL             HOST             客户端类型    方法类型                Referer关联计费开关    彩信模糊匹配    配置域名称    扩展头域名称

  testl7filtername     testl7filtername     URL       www.huawei.com  NULL             NULL        CONNECT&GET&POST    使能                 不使能          NULL           NULL
  testl7filtername2    testl7filtername2    HOST      NULL            www.example.com  NULL        CONNECT&GET&POST    使能                 不使能          NULL           NULL
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-L7FILTER.md`
