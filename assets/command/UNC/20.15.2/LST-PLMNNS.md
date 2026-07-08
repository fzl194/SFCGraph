---
id: UNC@20.15.2@MMLCommand@LST PLMNNS
type: MMLCommand
name: LST PLMNNS（查询网络切片）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PLMNNS
command_category: 查询类
applicable_nf:
- AMF
- SMF
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 运营商管理
- PLMN内网络切片管理
status: active
---

# LST PLMNNS（查询网络切片）

## 功能

**适用NF：AMF、SMF、SMSF**

该命令用于查询系统中的网络切片信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSIDX | 网络切片索引 | 可选必选说明：可选参数<br>参数含义：该参数用以在系统内唯一标识某个网络切片。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| PLMNIDX | PLMN索引 | 可选必选说明：可选参数<br>参数含义：该参数表示网络切片所归属运营商的Serving PLMN。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。PLMNIDX通过ADD NGSRVPLMN进行配置。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PLMNNS]] · 网络切片（PLMNNS）

## 使用实例

- 查询系统中“网络切片索引”为“0”的网络切片信息，执行如下命令：
  ```
  %%LST PLMNNS: NSIDX=0;%%
  RETCODE = 0  操作成功

  结果如下
  --------
          网络切片索引  =  0
             PLMN 索引  =  0
          切片业务类型  =  1
          切片细分标识  =  010101
              描述信息  =  NULL
                  状态  =  激活
      网络切片生效范围  =  全局网络
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中当前配置的所有网络切片信息，执行如下命令：
  ```
  %%LST PLMNNS:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  网络切片索引  PLMN 索引  切片业务类型  切片细分标识  描述信息  状态  网络切片生效范围 

  0             0          1             010101        NULL      激活  全局网络
  1             0          2             FFFFFF        NULL      激活  全局网络
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询网络切片（LST-PLMNNS）_09652528.md`
