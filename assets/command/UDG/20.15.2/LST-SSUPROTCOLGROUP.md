---
id: UDG@20.15.2@MMLCommand@LST SSUPROTCOLGROUP
type: MMLCommand
name: LST SSUPROTCOLGROUP（显示基于协议的质差检测策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SSUPROTCOLGROUP
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 智能板管理
- vvip
- 基于协议的质差策略
status: active
---

# LST SSUPROTCOLGROUP（显示基于协议的质差检测策略）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询基于协议的质差策略：

若要查询全部的基于协议的质差策略，请不要输入任何参数。

若要查询某个基于协议的质差策略，请输入“自定义协议组名称”。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEFPRTGRPNAME | 自定义协议组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定自定义的三级协议组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，不区分大小写，长度为1-63位。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [基于协议的质差检测策略（SSUPROTCOLGROUP）](configobject/UDG/20.15.2/SSUPROTCOLGROUP.md)

## 使用实例

- 假如运营商需要查询一条自定义协议组名称为testadc下基于协议的质差策略：
  ```
  %%LST SSUPROTCOLGROUP: DEFPRTGRPNAME="testadc";
  ```
  ```
  %%
  RETCODE = 0  操作成功

  基于协议的质差检测策略
  ----------------------
  自定义协议组名称  =  testadc
          协议名称  =  adc
        策略参数名  =  policyname
      业务流量特征  =  上下行均判断
  (结果个数 = 1)

  ---    END
  ```
- 假如运营商需要查询所有已配置的基于协议的质差策略：
  ```
  %%LST SSUPROTCOLGROUP:;
  ```
  ```
  %%
  RETCODE = 0  操作成功

  基于协议的质差检测策略
  ----------------------
  自定义协议组名称     协议名称  策略参数名   业务流量特征  

  testadc              adc       policyname   上下行均判断  
  ssuprotclogroupname  http      policyname2  上下行均判断  
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示基于协议的质差检测策略（LST-SSUPROTCOLGROUP）_15501061.md`
