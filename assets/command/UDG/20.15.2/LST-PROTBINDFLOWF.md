---
id: UDG@20.15.2@MMLCommand@LST PROTBINDFLOWF
type: MMLCommand
name: LST PROTBINDFLOWF（查询流过滤器协议绑定关系）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PROTBINDFLOWF
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
- 流过滤器管理
- 流过滤器的协议绑定
status: active
---

# LST PROTBINDFLOWF（查询流过滤器协议绑定关系）

## 功能

**适用NF：PGW-U、UPF**

此命令用于查询协议与流过滤器绑定关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [流过滤器协议绑定关系（PROTBINDFLOWF）](configobject/UDG/20.15.2/PROTBINDFLOWF.md)

## 使用实例

- 查询协议与名为testflowfiltername的流过滤器绑定关系：
  ```
  LST PROTBINDFLOWF:FLOWFILTERNAME="testflowfiltername";
  ```
  ```

  RETCODE = 0  操作成功。

  流过滤器协议绑定信息
  --------------------
    流过滤器名称  =  testflowfiltername
        协议名称  =  http
  七层过滤器名字  =  testl7filtername
  (结果个数 = 1)
  ---    END
  ```
- 查询协议与流过滤器所有的绑定关系：
  ```
  LST PROTBINDFLOWF:;
  ```
  ```

  RETCODE = 0  操作成功。

  流过滤器协议绑定信息
  --------------------
  流过滤器名称           协议名称    七层过滤器名字   

  testflowfiltername     http        testl7filtername 
  testflowfiltername2    http        testl7filtername2
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询流过滤器协议绑定关系（LST-PROTBINDFLOWF）_82837373.md`
