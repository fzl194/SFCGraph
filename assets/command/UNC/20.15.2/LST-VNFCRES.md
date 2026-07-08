---
id: UNC@20.15.2@MMLCommand@LST VNFCRES
type: MMLCommand
name: LST VNFCRES（查询VNFC内的资源配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VNFCRES
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 系统管理
- 资源管理
- 资源实例管理
status: active
---

# LST VNFCRES（查询VNFC内的资源配置信息）

## 功能

该命令用于查询VNFC内的资源配置信息。通过该命令可以查看各VNFC下部署的资源信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNFCNAME | VNFC名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示资源所在的VNFC名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，区分大小写。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@VNFCRES]] · VNFC内的资源配置信息（VNFCRES）

## 使用实例

- 查询所有资源配置信息：
  ```
  LST VNFCRES:;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  --------
  VNFC名称    逻辑资源编号    资源名称    VNFM分配的资源编号    VIM分配的资源编号                       资源实例类型    HA组    亲和性组    扩展组    主机位置    主机名称    资源类型    父资源名称                                虚拟节点模式

  VNFP        1               OMU1        NE=34618142           92a109d2-5aef-4f64-8c13-dd625d56aeaf    OMU             NULL    NULL        NULL      NULL        NULL        
  容器
        
  nps-omum-node-app-66a8e66e-0
            online
  VNFP        2               OMU2        NE=34618143           634cc600-486b-484c-a033-bb6ec1729c40    OMU             NULL    NULL        NULL      NULL        NULL        
  容器
        
  nps-omum-node-app-66a8e66e-0
            online
  (结果个数 = 2)
  ---    END
  ```
- 查询VNFC名称为VNFP的资源配置信息：
  ```
  LST VNFCRES:VNFCNAME="VNFP";
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  --------
  VNFC名称    逻辑资源编号    资源名称    VNFM分配的资源编号    VIM分配的资源编号                       资源实例类型    HA组    亲和性组    扩展组    主机位置    主机名称    资源类型    父资源名称                                虚拟节点模式

  VNFP        1               OMU1        NE=34618142           92a109d2-5aef-4f64-8c13-dd625d56aeaf    OMU             NULL    NULL        NULL      NULL        NULL        
  容器
        
  nps-omum-node-app-66a8e66e-0
            online
  VNFP        2               OMU2        NE=34618143           634cc600-486b-484c-a033-bb6ec1729c40    OMU             NULL    NULL        NULL      NULL        NULL        
  容器
        
  nps-omum-node-app-66a8e66e-0
            online
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-VNFCRES.md`
