---
id: UDG@20.15.2@MMLCommand@LST POLICYCONDITION
type: MMLCommand
name: LST POLICYCONDITION（显示业务质差检测策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: POLICYCONDITION
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 智能板管理
- vvip
- 质差检测策略
status: active
---

# LST POLICYCONDITION（显示业务质差检测策略）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询质差检测策略：

若要查询所有的质差检测策略，请不要输入任何参数。

若要查询某个质差检测策略，请输入“策略参数名”。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYCNDNAME | 策略参数名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务质量检测的策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，不区分大小写，长度1~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [业务质差检测策略（POLICYCONDITION）](configobject/UDG/20.15.2/POLICYCONDITION.md)

## 使用实例

- 假如运营商需要查询质差策略名为policyname的质差检测策略：
  ```
  %%LST POLICYCONDITION: POLICYCNDNAME="policyname";
  ```
  ```
  %%
  RETCODE = 0  操作成功

  质差检测策略
  ------------
                       策略参数名  =  policyname
    上行平均速率基线（Kbps）  =  100
    下行平均速率基线（Kbps）  =  NULL
       无线RTT基线值（毫秒）  =  NULL
        SP RTT基线值（毫秒）  =  NULL
       E2E RTT基线值（毫秒）  =  NULL
        上行大流阈值（Kbps）  =  NULL
        下行大流阈值（Kbps）  =  NULL
          多指标质差判断逻辑  =  所有条件不满足
  (结果个数 = 1)

  ---    END
  ```
- 假如运营商需要查询全部的质差检测策略：
  ```
  %%LST POLICYCONDITION:;
  ```
  ```
  %%
  RETCODE = 0  操作成功

  质差检测策略
  ------------
  策略参数名   上行平均速率基线（Kbps）  下行平均速率基线（Kbps）  无线RTT基线值（毫秒）  SP RTT基线值（毫秒）  E2E RTT基线值（毫秒）  上行大流阈值（Kbps）  下行大流阈值（Kbps）  多指标质差判断逻辑  

  policyname   100                       NULL                      NULL                   NULL                  NULL                   NULL                  NULL                  所有条件不满足      
  policyname2  NULL                      100                       NULL                   NULL                  NULL                   NULL                  NULL                  所有条件不满足      
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示业务质差检测策略（LST-POLICYCONDITION）_15501063.md`
