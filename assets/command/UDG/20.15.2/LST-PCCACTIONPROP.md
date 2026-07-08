---
id: UDG@20.15.2@MMLCommand@LST PCCACTIONPROP
type: MMLCommand
name: LST PCCACTIONPROP（查询PCC动作属性）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PCCACTIONPROP
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- PCC控制策略
- PCC动作属性
status: active
---

# LST PCCACTIONPROP（查询PCC动作属性）

## 功能

**适用NF：PGW-U、UPF**

此命令用于查询PCC动作属性。

支持批量查询，不输入查询条件，表示查询已经配置的所有PCC动作属性。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCCACTPROPNAME | PCC动作属性名称 | 可选必选说明：可选参数<br>参数含义：设置PCC动作属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PCCACTIONPROP]] · PCC动作属性（PCCACTIONPROP）

## 使用实例

- 查询名称为test_pccact_1的PCC动作属性：
  ```
  LST PCCACTIONPROP: PCCACTPROPNAME="test_pccact_1";
  ```
  ```

  RETCODE = 0  操作成功。

  PCC动作属性信息
  ---------------
     PCC动作属性名称  =  test_pccact_1
  上行发起重定向名称  =  test_redirect
    上行发起上行门控  =  Pass
    上行发起下行门控  =  Pass
  下行发起重定向名称  =  NULL
    下行发起上行门控  =  Discard
    下行发起下行门控  =  Discard
          配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询所有的PCC动作属性：
  ```
  LST PCCACTIONPROP:;
  ```
  ```

  RETCODE = 0  操作成功。

  PCC动作属性信息
  ---------------
  PCC动作属性名称    上行发起重定向名称    上行发起上行门控    上行发起下行门控    下行发起重定向名称    下行发起上行门控    下行发起下行门控    配置域名称
  test_pccact_1      test_redirect         Discard             Discard             NULL                  Pass                Pass                NULL
  test_pccact_2      NULL                  Pass                Pass                test_caqos            Discard             Discard             NULL
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-PCCACTIONPROP.md`
