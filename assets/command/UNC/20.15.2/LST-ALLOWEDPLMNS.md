---
id: UNC@20.15.2@MMLCommand@LST ALLOWEDPLMNS
type: MMLCommand
name: LST ALLOWEDPLMNS（查询允许访问的PLMN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ALLOWEDPLMNS
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 授权管理
- 访问授权控制
- PLMN访问授权控制
status: active
---

# LST ALLOWEDPLMNS（查询允许访问的PLMN）

## 功能

**适用NF：NRF**

该命令用于查询指定NF对象允许访问的PLMN信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OBJNAME | 授权对象名称 | 可选必选说明：可选参数<br>参数含义：该参数表示设置访问授权控制的NF对象名称。该参数可通过LST ALLOWEDOBJNAME命令获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ALLOWEDPLMNS]] · 允许访问的PLMN（ALLOWEDPLMNS）

## 使用实例

- 查询所有对象允许访问的PLMN信息：
  ```
  LST ALLOWEDPLMNS:;
  %%LST ALLOWEDPLMNS:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  授权对象名称   允许访问该对象的移动国家码  允许访问该对象的移动网号  记录状态  
  objname001     123                         02                        提交状态     
  objname002     123                         45                        提交状态      
  (结果个数 = 2)
  ```
- 查询NF对象objname001允许访问的PLMN信息：
  ```
  LST ALLOWEDPLMNS: OBJNAME="objname001";
  %%LST ALLOWEDPLMNS: OBJNAME="objname001";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
                授权对象名称  =  objname001
  允许访问该对象的移动国家码  =  123
    允许访问该对象的移动网号  =  02
                    记录状态  =  提交状态
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询允许访问的PLMN（LST-ALLOWEDPLMNS）_09653100.md`
