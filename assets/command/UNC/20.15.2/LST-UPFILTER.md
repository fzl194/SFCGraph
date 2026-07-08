---
id: UNC@20.15.2@MMLCommand@LST UPFILTER
type: MMLCommand
name: LST UPFILTER（查询UPF过滤组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPFILTER
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP过滤组绑定管理
status: active
---

# LST UPFILTER（查询UPF过滤组）

## 功能

**适用NF：SMF**

该命令用于查询UPF过滤组信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | UPF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于标识UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：无 |
| DNN | DNN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~66。不区分大小写，转成小写存储，可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字和字母，不能出现连续两个“.”。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPFILTER]] · UPF过滤组（UPFILTER）

## 使用实例

- 查询所有UPF过滤组信息：
  ```
  %%LST UPFILTER:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  UPF实例名称  =  upf1
      DNN名称  =  huawei.com
     过滤组ID  =  1
  (结果个数 = 1)

  ---    END
  ```
- 查询指定UPF实例名为“UP1”的信息：
  ```
  %%LST UPFILTER: NFINSTANCENAME="UP1";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  UPF实例名称  =  up1
      DNN名称  =  huawei.com
     过滤组ID  =  1
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UPFILTER.md`
