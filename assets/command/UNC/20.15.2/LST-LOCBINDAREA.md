---
id: UNC@20.15.2@MMLCommand@LST LOCBINDAREA
type: MMLCommand
name: LST LOCBINDAREA（查询UPF位置信息与该UPF优先支持的服务区的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LOCBINDAREA
command_category: 查询类
applicable_nf:
- SMF
- SGW-C
- GGSN
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- 位置区域绑定本地优选名称
status: active
---

# LST LOCBINDAREA（查询UPF位置信息与该UPF优先支持的服务区的绑定关系）

## 功能

**适用NF：SMF、SGW-C、GGSN、PGW-C**

该命令用于查询UPF位置信息与该UPF优先支持的服务区的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCALITY | UPF位置区 | 可选必选说明：可选参数<br>参数含义：该参数用于标识UPF位置区。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~150。<br>默认值：无<br>配置原则：<br>该参数需要与ADD PNFPROFILE命令中 “LOCALITY”的取值保持一致，参数匹配时大小写不敏感。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCBINDAREA]] · UPF位置信息与该UPF优先支持的服务区的绑定关系（LOCBINDAREA）

## 使用实例

- 查询所有的UPF位置信息与UPF优先支持的服务区的绑定关系： LST LOCBINDAREA:;
  ```
  %%LST LOCBINDAREA:;%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
  UPF位置区  UPF服务区名称  

  locality1  area1                  
  locality2  area2                  
  (结果个数 = 2)
  ```
- 查询特定的UPF位置信息与该UPF优先支持的服务区的绑定关系，其中UPF位置区为“locality1”： LST LOCBINDAREA: LOCALITY="locality1";
  ```
  %%LST LOCBINDAREA: LOCALITY="locality1";%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
      UPF位置区  =  locality1
  UPF服务区名称  =  area1
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LOCBINDAREA.md`
