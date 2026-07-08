---
id: UNC@20.15.2@MMLCommand@LST STCNFPROFILE
type: MMLCommand
name: LST STCNFPROFILE（查询手动注册的NFProfile）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: STCNFPROFILE
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- NF信息导入管理
status: active
---

# LST STCNFPROFILE（查询手动注册的NFProfile）

## 功能

**适用NF：NRF**

该命令用于查询在NRF上手动注册的NF实例。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示手动注册的NF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：无 |
| ROFILEFILENAME | 手动注册的NFPROFILE文件名 | 可选必选说明：可选参数<br>参数含义：该参数用于表示手动注册NF实例时使用文件名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@STCNFPROFILE]] · 手动注册的NFProfile（STCNFPROFILE）

## 使用实例

- 查询所有的手动注册NF实例：
  ```
  LST STCNFPROFILE:;
  %%LST STCNFPROFILE:;%%
  RETCODE = 0  执行成功
  操作结果如下:
  -------------------------
  NF实例标识                            手动注册的NFPROFILE文件名   更新时间        
  f717585b-cb76-484c-9302-6e9ce69d5623  ausf12.json                 2020-05-19 22:11:26  
  f717585b-cb76-484c-9302-6e9ce69d5624  ausf13.json                 2020-05-21 17:48:44  
  f717585b-cb76-484c-9302-6e9ce69d5625  ausf14.json                 2020-05-21 17:48:44  
  (结果个数 = 3)
  ```
- 查询NF实例标识为“f717585b-cb76-484c-9302-6e9ce69d5623”的手动注册NF实例：
  ```
  LST STCNFPROFILE: NFINSTANCEID="f717585b-cb76-484c-9302-6e9ce69d5623";
  %%LST STCNFPROFILE: NFINSTANCEID="f717585b-cb76-484c-9302-6e9ce69d5623";%%
  RETCODE = 0  执行成功
  操作结果如下:
  -------------------------
                  NF实例标识 = f717585b-cb76-484c-9302-6e9ce69d5623
  手动注册的NFPROFILE文件名  = ausf12.json
                   更新时间  = 2020-05-21 17:46:44
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-STCNFPROFILE.md`
