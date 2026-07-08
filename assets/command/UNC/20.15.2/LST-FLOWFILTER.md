---
id: UNC@20.15.2@MMLCommand@LST FLOWFILTER
type: MMLCommand
name: LST FLOWFILTER（查询流过滤器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: FLOWFILTER
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务过滤器
- 流过滤器
status: active
---

# LST FLOWFILTER（查询流过滤器）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询所有的流过滤器实例，或者查询指定名称的流过滤器。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置“流过滤器名称”， 该参数可供RULE命令中的“流过滤器名称”参数引用。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FLOWFILTER]] · 流过滤器（FLOWFILTER）

## 使用实例

- 查询名为“testflowfiltername”的流过滤器：
  ```
  LST FLOWFILTER:FLOWFILTERNAME="testflowfiltername";
  ```
  ```
  %
  RETCODE = 0  操作成功。

  流过滤器信息
  ------------
       流过滤器名称  =  testflowfiltername
  (结果个数 = 1)
  ---    END
  ```
- 查询所有的流过滤器：
  ```
  LST FLOWFILTER:;
  ```
  ```

  RETCODE = 0  操作成功。

  流过滤器信息
  ------------
  流过滤器名称         

  testflowfilter                
  testflowfiltername   
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询流过滤器（LST-FLOWFILTER）_09897155.md`
