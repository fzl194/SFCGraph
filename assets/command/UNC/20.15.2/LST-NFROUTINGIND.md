---
id: UNC@20.15.2@MMLCommand@LST NFROUTINGIND
type: MMLCommand
name: LST NFROUTINGIND（查询选路指示器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFROUTINGIND
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- 号段配置管理
- 选路指示器号段管理
status: active
---

# LST NFROUTINGIND（查询选路指示器）

## 功能

**适用NF：NRF**

该命令用于在NRF上查询选路指示器。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFGROUPID | NF组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示支持ROUTIINGIND号段的NF组标识，该参数可以通过LST NFGROUP命令查看。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~128。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成，不区分大小写。<br>默认值：无<br>配置原则：无 |
| ROUTINGIND | 选路指示器 | 可选必选说明：可选参数<br>参数含义：该参数用于表示支持ROUTIINGIND号段信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~4。取值范围0-9999。<br>默认值：无<br>配置原则：<br>当NF组支持ROUTINGIND为通配时，需要将ROUTINGIND设置为ALL。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFROUTINGIND]] · 选路指示器（NFROUTINGIND）

## 使用实例

- 查询所有的选路指示器信息：
  ```
  %%LST NFROUTINGIND:;%%
  RETCODE = 0  执行成功

  结果如下
  -------------------------
   NF组标识       选路指示器     

   nfgroup001     1000
   nfgroup002     1050
                        
  (结果个数 = 2)
  ```
- 查询NFGROUPID为nfgroup001的选路指示器信息：
  ```
  %%LST NFROUTINGIND:NFGROUPID="nfgroup001";%%
  RETCODE = 0  执行成功

  结果如下
  -------------------------
     NF组标识 = nfgroup001
   选路指示器 = 1000               

  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NFROUTINGIND.md`
